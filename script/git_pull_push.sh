#!/bin/sh
cd
pg_dump -U tyrsadocto -h pg3.sweb.ru > git/kupiflakon/postgres/kupiflakon.dump
cd git/kupiflakon
git pull
git add *
git commit * -m 'dump base'
git push
pg_ctl -D $PREFIX/var/lib/postgresql stop
exit
