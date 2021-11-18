-- script that creates the mysql server user
CREATE USER IF NOT EXISTS `user_0d_1`@`localhost` IDENTIFIED BY `user_0d_1_pwd`;
GRANT ALL PRIVILEGES ON *.* TO `user_0d_01`@`localhost`;
FLUSH PRIVILEGES;