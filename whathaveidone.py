#!/usr/local/bin/python3
# coding=UTF-8

import sys, getopt
import time
import sqlite3
import os, signal


def convert_time(t):
    if ':' in t:
        _ = t.split(':')
        return str(_[0] * 3600 + _[1] * 60 + _[2])
    if ':' not in t:
        _ = int(t)
        h = str(_ // 3600)
        m = str((_ % 3600) // 60)
        s = str(_ % 60)
        return h + ':' + m + ':' + s


def open_db():
    db = sqlite3.connect('whathaveidone.db')
    return db


def close_db(db):
    db.close()


def show_help():
    help = '-h\t\tshow help.\n-l\t\tshow all tasks.\n-g <take_name>\tshow specific info of <task_name>.\n-n <task_name>\tcreat a new task.\n-d <task_name>\tdelete <task_name>.\n-s <task_name>\tstart timing.\n-e <task_name>\tend timing.'
    print(help)


def show_done(task_name=None):
    if task_name:
        db = open_db()
        cs = db.cursor()
        sql = 'select task_time from tasks where task_name = "%s";' % (task_name,)
        try:
            cs.execute(sql)

            for res in cs.fetchall():
                print(task_name + '\t' + convert_time(res[0]))
        except:
            print('Failed.')

        close_db(db)


    else:
        db = open_db()
        cs = db.cursor()
        sql = 'select * from tasks;'
        try:
            cs.execute(sql)

            for res in cs.fetchall():
                print(res[0] + '\t' + convert_time(res[1]))
        except:
            print('Failed.')

        close_db(db)


def creat_task(task_name):
    db = open_db()
    cs = db.cursor()

    sql = 'insert into tasks values ("%s","%s");' % (task_name, '0')
    try:
        cs.execute(sql)
        db.commit()
    except:
        print('Create task failed.')

    print('Create task %s successfully.' % (task_name,))

    close_db(db)


def delete_task(task_name=None):
    db = open_db()
    cs = db.cursor()

    sql = 'delete from tasks where task_name="%s";' % (task_name,)
    try:
        cs.execute(sql)
        db.commit()
    except:
        print('Delete task failed.')

    print('Delete task %s successfully' % (task_name,))

    close_db(db)


def start_task(task_name):
    # 流程：先根据任务名判断任务是否存在，若存在，则记录子进程pid和当前时间，记入pid_time.txt
    # 若任务不存在，则提示-n创建任务。
    def handle_exit(signum, _):
        if signum == signal.SIGTERM:
            sys.exit(0)
        sys.exit(1)

    signal.signal(signal.SIGINT, handle_exit)
    signal.signal(signal.SIGTERM, handle_exit)

    db = open_db()
    cs = db.cursor()

    check_sql = 'select task_name from tasks where task_name="%s";' % (task_name,)
    cs.execute(check_sql)

    # 任务存在,可以计时
    if cs.fetchall() != []:
        f = open('pid_time.txt', 'r')
        # 文件里啥也没有  说明当前没有任务在计时
        if not f.read():
            f.close()

            def handle_exit(signum, _):
                if signum == signal.SIGTERM:
                    sys.exit(0)
                sys.exit(1)

            signal.signal(signal.SIGINT, handle_exit)
            signal.signal(signal.SIGTERM, handle_exit)

            pid = os.fork()

            # 父进程
            if pid > 0:
                time.sleep(5)
                sys.exit(0)

            # 子进程
            ppid = os.getppid()
            pid = os.getpid()

            if write_pid_file(pid) != 0:
                os.kill(ppid, signal.SIGINT)
                sys.exit(1)

            os.setsid()
            signal.signal(signal.SIG_IGN, signal.SIGHUP)

            print('Timing started.')
            os.kill(ppid, signal.SIGTERM)
        # 文件中有ID号 说明有程序正在运行
        else:
            f.close()
            print('A task is still timing, stop it first.')
    # 任务不存在,先创建
    else:
        print('Task dose not exists. U can try -n to create a task.')

    db.close()


def write_pid_file(pid):
    print('pid:' + str(pid))
    try:
        f = open('pid_time.txt', 'w+')
        f.write(str(pid) + '\n' + str(int(time.time())))
        f.close()
        return 0
    except:
        return -1


def end_task(task_name):
    f = open('pid_time.txt', 'r')
    pid = f.readline()

    # 当前没有任务在执行
    if pid == '':
        print('No task is running.')
        f.close()
        return

    try:
        os.kill(pid, signal.SIGTERM)
        print('Task stopped.')
    except:
        print('Stop task failed.')
        f.close()
        return

    start_time = int(f.readline())
    f.close()

    hold_time = int(time.time() - start_time)

    db = open_db()
    cs = db.cursor()

    get_time_sql = 'select task_time from tasks where task_name = "%s";' % (task_name,)
    cs.execute(get_time_sql)
    rows = cs.fetchall()

    # 任务存在，可以结束
    if rows != []:
        _ = int(rows[0][0])
        sql = 'update tasks set task_time="%s" where task_name="%s";' % (str(_ + hold_time), task_name)
        cs.execute(sql)
        db.commit()
        print('Task time updated.')
    # 任务不存在，没法结束
    else:
        print('Task time update error.')

    db.close()


if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], 'hlg:n:d:s:e:')

    for opt, arg in opts:
        if opt == '-h':
            show_help()
        elif opt == '-l':
            show_done()
        elif opt == '-g':
            show_done(arg)
        elif opt == '-n':
            creat_task(arg)
        elif opt == '-d':
            delete_task(arg)
        elif opt == '-s':
            start_task(arg)
        elif opt == '-e':
            end_task(arg)
