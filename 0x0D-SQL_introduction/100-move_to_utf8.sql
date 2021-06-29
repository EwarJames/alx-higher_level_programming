-- Converts hbtn_0c_0 database to utf8
USE `hbtn_0c_0`
ALTER TABLE `first_table`
CONVERT TO CHARACTERSET utf8mb4 COLLATE utf8_mb4_unicode_ci; 
