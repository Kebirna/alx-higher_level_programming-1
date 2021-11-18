-- script that creates the db hbtn_0d_2 and the user_0d_2
CREATE database IF NOT EXISTS `hbtn_0d_2`;
CREATE user IF NOT EXISTS `user_0d_2`@`localhost` IDENTIFIED BY `user_0d_2_pwd`;
GRANT SELECT ON `hbtn_0d_2`.* TO `user_0d_2`@`localhost` IDENTIFIED BY `user_0d_2_pwd`;
flush PRIVILEGES;