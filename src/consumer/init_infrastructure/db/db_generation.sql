-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema users_db
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `users_db` ;

-- -----------------------------------------------------
-- Schema users_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `users_db` DEFAULT CHARACTER SET utf8 ;
USE `users_db` ;

-- -----------------------------------------------------
-- Table `users_db`.`users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `users_db`.`users` ;

CREATE TABLE IF NOT EXISTS `users_db`.`users` (
  `username` VARCHAR(45) NOT NULL,
  `password` VARCHAR(64) NOT NULL,
  `salt` VARCHAR(64) NOT NULL,
  PRIMARY KEY (`username`))
ENGINE = InnoDB;

USE `users_db` ;

-- -----------------------------------------------------
-- procedure sign_up
-- -----------------------------------------------------

USE `users_db`;
DROP procedure IF EXISTS `users_db`.`sign_up`;

DELIMITER $$
USE `users_db`$$
CREATE PROCEDURE `sign_up` (in usrname varchar(45), in pass varchar(64), in s varchar(64))
BEGIN
	insert into users (username, password, salt)
    values (usrname, pass, s);
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure log_in
-- -----------------------------------------------------

USE `users_db`;
DROP procedure IF EXISTS `users_db`.`log_in`;

DELIMITER $$
USE `users_db`$$
CREATE PROCEDURE `log_in` (in usr varchar(45), in pass varchar(64))
BEGIN
	declare pw varchar(64);
    #set pw = null;
    select password
    from users
    where username = usr
    into pw;
    
    if pw is null or pw != pass then
		signal sqlstate '45999'
		set message_text = "Error: wrong username or password.";
    end if; 
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure get_user_list
-- -----------------------------------------------------

USE `users_db`;
DROP procedure IF EXISTS `users_db`.`get_user_list`;

DELIMITER $$
USE `users_db`$$
CREATE PROCEDURE `get_user_list` ()
BEGIN
	select username from users;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure get_salt
-- -----------------------------------------------------

USE `users_db`;
DROP procedure IF EXISTS `users_db`.`get_salt`;

DELIMITER $$
USE `users_db`$$
CREATE PROCEDURE `get_salt` (in user varchar(45), out slt varchar(64))
BEGIN
	set slt = null;
    
	select salt 
    from users
    where username = user
    into slt;
    
    if slt is null then
		signal sqlstate '45999'
		set message_text = "Error: wrong username or password.";
    end if; 
END$$

DELIMITER ;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
USE `users_db`;

DELIMITER $$

USE `users_db`$$
DROP TRIGGER IF EXISTS `users_db`.`users_BEFORE_INSERT` $$
USE `users_db`$$
CREATE DEFINER = CURRENT_USER TRIGGER `users_db`.`users_BEFORE_INSERT` BEFORE INSERT ON `users` FOR EACH ROW
BEGIN
	declare is_present varchar(45);
    declare new_username varchar(45);
    
    set new_username = NEW.username;
    
    select username
    from users 
    where username = new_username
    into is_present;
    
    if is_present is not null then
		signal sqlstate '45999'
		set message_text = "Error: username still present.";
    end if;

END$$


DELIMITER ;
