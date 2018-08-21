import pymysql

if __name__ == '__main__':
        # 创建连接
        conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='zytdb')
        # 创建游标
        cursor = conn.cursor()
        values = '''
                   create table IF NOT EXISTS MTime (
                    `id` INT(20) NOT NULL AUTO_INCREMENT,
                    `MovieId` INT(20) DEFAULT NULL,
                    `MovieTitle` VARCHAR(20) DEFAULT NULL,
                    `RatingFinal` VARCHAR(20) DEFAULT NULL,
                    `ROtherFinal` VARCHAR(20) DEFAULT NULL,
                    `RPictureFinal` VARCHAR(20) DEFAULT NULL,
                    `RDirectorFinal` VARCHAR(20) DEFAULT NULL,
                    `RStoryFinal` VARCHAR(20) DEFAULT NULL,
                    `Usercount` INT(20) DEFAULT NULL,
                    `AttitudeCount` INT(20) DEFAULT NULL,
                    `TotalBoxOffice` INT(20) DEFAULT NULL,
                    `TodayBoxOffice` INT(20) DEFAULT NULL,
                    `Rank` INT(20) DEFAULT NULL,
                    `ShowDays` INT(20) DEFAULT NULL,
                    `isRelease` TINYINT(2) DEFAULT NULL,
                    PRIMARY KEY (`id`)
                   )  ENGINE=INNODB AUTO_INCREMENT=75 DEFAULT CHARSET=utf8
                '''
        # 创建游标
        # cursor.execute(values)

        sql = "INSERT INTO MTime (MovieId, MovieTitle) values (%s,%s)"
        cursor.execute(sql, [1, 2])
        conn.commit()
        conn.close()

