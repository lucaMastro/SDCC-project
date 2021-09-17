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
  `password` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`username`))
ENGINE = InnoDB;

USE `users_db` ;

-- -----------------------------------------------------
-- procedure sign_in
-- -----------------------------------------------------

USE `users_db`;
DROP procedure IF EXISTS `users_db`.`sign_in`;

DELIMITER $$
USE `users_db`$$
CREATE PROCEDURE `sign_in` (in usrname varchar(45), in pass varchar(45))
BEGIN
	insert into users (username, password)
    values (usrname, pass);
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure log_in
-- -----------------------------------------------------

USE `users_db`;
DROP procedure IF EXISTS `users_db`.`log_in`;

DELIMITER $$
USE `users_db`$$
CREATE PROCEDURE `log_in` (in usr varchar(45), in pass varchar(45), out ok bool)
BEGIN
	declare pw varchar(45);
    select password
    from users
    where username = usr
    into pw;
    
    if pw is null or pw != pass then
		set ok = False;
    else
		set ok = True;
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

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- -----------------------------------------------------
-- Data for table `users_db`.`users`
-- -----------------------------------------------------
START TRANSACTION;
USE `users_db`;
INSERT INTO `users_db`.`users` (`username`, `password`) VALUES ('Luca', 'prova');

COMMIT;

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
		set message_text = "error: username still present.";
    end if;

END$$


DELIMITER ;
