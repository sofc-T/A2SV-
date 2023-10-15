SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema project_management_tool
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema project_management_tool
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `project_management_tool` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `project_management_tool` ;

-- -----------------------------------------------------
-- Table `project_management_tool`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project_management_tool`.`users` (
  `user_id` INT NOT NULL AUTO_INCREMENT,
  `user_name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `created_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `full_name` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`user_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 9
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `project_management_tool`.`projects`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project_management_tool`.`projects` (
  `project_id` INT NOT NULL AUTO_INCREMENT,
  `project_name` VARCHAR(255) NOT NULL,
  `project_description` TEXT NULL DEFAULT NULL,
  `start_date` DATE NULL DEFAULT NULL,
  `end_date` DATE NULL DEFAULT NULL,
  `version_control_system` VARCHAR(255) NULL DEFAULT NULL,
  `repository_url` VARCHAR(255) NULL DEFAULT NULL,
  `created_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `user_id` INT NULL DEFAULT NULL,
  `read_me` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`project_id`),
  INDEX `fk_user_id` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `project_management_tool`.`users` (`user_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

-- -----------------------------------------------------
-- Table `project_management_tool`.`forked_projects`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `project_management_tool`.`forked_projects` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `main_project_id` INT NULL DEFAULT NULL,
  `forked_project_name` VARCHAR(255) NULL DEFAULT NULL,
  `forked_project_description` TEXT NULL DEFAULT NULL,
  `forked_by_user_id` INT NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `main_project_id` (`main_project_id` ASC) VISIBLE,
  INDEX `forked_by_user_id` (`forked_by_user_id` ASC) VISIBLE,
  CONSTRAINT `forked_projects_ibfk_1`
    FOREIGN KEY (`main_project_id`)
    REFERENCES `project_management_tool`.`projects` (`project_id`),
  CONSTRAINT `forked_projects_ibfk_2`
    FOREIGN KEY (`forked_by_user_id`)
    REFERENCES `project_management_tool`.`users` (`user_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `project_management_tool`.`issues`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project_management_tool`.`issues` (
  `issue_id` INT NOT NULL AUTO_INCREMENT,
  `issue_name` VARCHAR(255) NOT NULL,
  `issue_description` TEXT NULL DEFAULT NULL,
  `status` VARCHAR(20) NULL DEFAULT NULL,
  `project_id` INT NULL DEFAULT NULL,
  `issued_by` INT NULL DEFAULT NULL,
  `created_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`issue_id`),
  INDEX `project_id` (`project_id` ASC) VISIBLE,
  CONSTRAINT `issues_ibfk_1`
    FOREIGN KEY (`project_id`)
    REFERENCES `project_management_tool`.`projects` (`project_id`),
  CONSTRAINT `issues_ibfk_2`
	FOREIGN KEY (`issued_by`)
    REFERENCES `project_management_tool`.`users` (`user_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

-- -----------------------------------------------------
-- Table `project_management_tool`.`programming_languages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project_management_tool`.`programming_languages` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `language` VARCHAR(50) NULL DEFAULT NULL,
  `project_id` INT NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `project_id` (`project_id` ASC) VISIBLE,
  CONSTRAINT `programming_languages_ibfk_1`
    FOREIGN KEY (`project_id`)
    REFERENCES `project_management_tool`.`projects` (`project_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `project_management_tool`.`pull_requests`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project_management_tool`.`pull_requests` (
  `pull_request_id` INT NOT NULL,
  `pull_request_name` VARCHAR(255) NOT NULL,
  `pull_request_description` TEXT NULL DEFAULT NULL,
  `status` VARCHAR(20) NULL DEFAULT NULL,
  `project_id` INT NULL DEFAULT NULL,
  `requested_by` INT NULL DEFAULT NULL,
  `created_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`pull_request_id`),
  INDEX `project_id` (`project_id` ASC) VISIBLE,
  CONSTRAINT `pull_requests_ibfk_1`
    FOREIGN KEY (`project_id`)
    REFERENCES `project_management_tool`.`projects` (`project_id`),
  CONSTRAINT `pull_requests_ibfk_2`
    FOREIGN KEY (`requested_by`)
    REFERENCES `project_management_tool`.`users` (`user_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `project_management_tool`.`pull_request_assignments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project_management_tool`.`pull_request_assignments` (
  `user_id` INT NOT NULL,
  `pull_request_id` INT NOT NULL,
  PRIMARY KEY (`user_id`, `pull_request_id`),
  INDEX `pull_request_id` (`pull_request_id` ASC) VISIBLE,
  CONSTRAINT `pull_request_assignments_ibfk_1`
    FOREIGN KEY (`user_id`)
    REFERENCES `project_management_tool`.`users` (`user_id`),
  CONSTRAINT `pull_request_assignments_ibfk_2`
    FOREIGN KEY (`pull_request_id`)
    REFERENCES `project_management_tool`.`pull_requests` (`pull_request_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;
-- -----------------------------------------------------
-- Table `project_management_tool`.`user_assignment`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project_management_tool`.`user_assignment` (
  `user_id` INT NOT NULL,
  `task_id` INT NOT NULL,
  PRIMARY KEY (`user_id`, `task_id`),
  INDEX `task_id` (`task_id` ASC) VISIBLE,
  CONSTRAINT `user_assignment_ibfk_1`
    FOREIGN KEY (`user_id`)
    REFERENCES `project_management_tool`.`users` (`user_id`),
  CONSTRAINT `user_assignment_ibfk_2`
    FOREIGN KEY (`task_id`)
    REFERENCES `project_management_tool`.`tasks` (`task_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

-- -----------------------------------------------------
-- Table `project_management_tool`.`tasks`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project_management_tool`.`tasks` (
  `task_id` INT NOT NULL AUTO_INCREMENT,
  `task_name` VARCHAR(255) NOT NULL,
  `task_description` TEXT NULL DEFAULT NULL,
  `start_date` DATE NULL DEFAULT NULL,
  `end_date` DATE NULL DEFAULT NULL,
  `status` VARCHAR(20) NULL DEFAULT NULL,
  `project_id` INT NULL DEFAULT NULL,
  `created_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `user_name` VARCHAR(255) NULL DEFAULT NULL,
  `assigned_to` INT NULL DEFAULT NULL,
  `project_name` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`task_id`),
  INDEX `project_id` (`project_id` ASC) VISIBLE,
  CONSTRAINT `tasks_ibfk_1`
    FOREIGN KEY (`project_id`)
    REFERENCES `project_management_tool`.`projects` (`project_id`),
  CONSTRAINT `tasks_ibfk_2`
    FOREIGN KEY (`assigned_to`)
    REFERENCES `project_management_tool`.`users` (`user_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- Insert random data into `users` table
INSERT INTO `users` (user_name, email, password, full_name)
SELECT 
    CONCAT('user', id) AS user_name,
    CONCAT('user', id, '@example.com') AS email,
    CONCAT('pass', id) AS password,
    CONCAT('Full Name ', id) AS full_name
FROM
    (SELECT 1 AS id UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4 UNION ALL SELECT 5 UNION ALL SELECT 6 UNION ALL SELECT 7 UNION ALL SELECT 8 UNION ALL SELECT 9 UNION ALL SELECT 10) AS dummy;

-- Insert random data into `projects` table
INSERT INTO `projects` (project_id, project_name, project_description, start_date, end_date, version_control_system, repository_url, user_id, read_me)
SELECT 
    id AS project_id,
    CONCAT('Project ', id) AS project_name,
    CONCAT('Description for Project ', id) AS project_description,
    DATE_ADD(CURRENT_DATE(), INTERVAL -FLOOR(RAND() * 365) DAY) AS start_date,
    DATE_ADD(CURRENT_DATE(), INTERVAL FLOOR(RAND() * 365) DAY) AS end_date,
    'Git' AS version_control_system,
    CONCAT('https://github.com/project', id) AS repository_url,
    (SELECT user_id FROM `users` ORDER BY RAND() LIMIT 1) AS user_id,
    CONCAT('ReadMe for Project ', id) AS read_me
FROM
    (SELECT 1 AS id UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4 UNION ALL SELECT 5 UNION ALL SELECT 6 UNION ALL SELECT 7 UNION ALL SELECT 8 UNION ALL SELECT 9 UNION ALL SELECT 10) AS dummy;

-- Insert random data into `forked_projects` table
INSERT INTO `forked_projects` (main_project_id, forked_project_name, forked_project_description, forked_by_user_id)
SELECT 
    (SELECT project_id FROM `projects` ORDER BY RAND() LIMIT 1) AS main_project_id,
    CONCAT('Forked Project ', id) AS forked_project_name,
    CONCAT('Description for Forked Project ', id) AS forked_project_description,
    (SELECT user_id FROM `users` ORDER BY RAND() LIMIT 1) AS forked_by_user_id
FROM
    (SELECT 1 AS id UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4 UNION ALL SELECT 5 UNION ALL SELECT 6 UNION ALL SELECT 7 UNION ALL SELECT 8 UNION ALL SELECT 9 UNION ALL SELECT 10) AS dummy;

-- Insert random data into `issues` table
INSERT INTO `issues` (issue_name, issue_description, status, project_id, issued_by)
SELECT 
    CONCAT('Issue ', id) AS issue_name,
    CONCAT('Description for Issue ', id) AS issue_description,
    CASE FLOOR(RAND() * 3)
        WHEN 0 THEN 'Open'
        WHEN 1 THEN 'In Progress'
        ELSE 'Closed'
    END AS status,
    (SELECT project_id FROM `projects` ORDER BY RAND() LIMIT 1) AS project_id,
    (SELECT user_id FROM `users` ORDER BY RAND() LIMIT 1) AS issued_by
FROM
    (SELECT 1 AS id UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4 UNION ALL SELECT 5 UNION ALL SELECT 6 UNION ALL SELECT 7 UNION ALL SELECT 8 UNION ALL SELECT 9 UNION ALL SELECT 10) AS dummy;


-- Insert random data into `pull_requests` table
INSERT INTO `pull_requests` (pull_request_id, pull_request_name, pull_request_description, status, project_id, requested_by)
SELECT 
    id AS pull_request_id,
    CONCAT('Pull Request ', id) AS pull_request_name,
    CONCAT('Description for Pull Request ', id) AS pull_request_description,
    CASE FLOOR(RAND() * 3)
        WHEN 0 THEN 'Open'
        WHEN 1 THEN 'Merged'
        ELSE 'Closed'
    END AS status,
    (SELECT project_id FROM `projects` ORDER BY RAND() LIMIT 1) AS project_id,
    (SELECT user_id FROM `users` ORDER BY RAND() LIMIT 1) AS requested_by
FROM
    (SELECT 1 AS id UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4 UNION ALL SELECT 5 UNION ALL SELECT 6 UNION ALL SELECT 7 UNION ALL SELECT 8 UNION ALL SELECT 9 UNION ALL SELECT 10) AS dummy;


-- Insert random data into `tasks` table
INSERT INTO `tasks` (task_id, task_name, task_description, start_date, end_date, status, project_id, user_name, assigned_to, project_name)
SELECT 
    id AS task_id,
    CONCAT('Task ', id) AS task_name,
    CONCAT('Description for Task ', id) AS task_description,
    DATE_ADD(CURRENT_DATE(), INTERVAL -FLOOR(RAND() * 365) DAY) AS start_date,
    DATE_ADD(CURRENT_DATE(), INTERVAL FLOOR(RAND() * 365) DAY) AS end_date,
    CASE FLOOR(RAND() * 3)
        WHEN 0 THEN 'Open'
        WHEN 1 THEN 'In Progress'
        ELSE 'Completed'
    END AS status,
    (SELECT project_id FROM `projects` ORDER BY RAND() LIMIT 1) AS project_id,
    (SELECT user_name FROM `users` ORDER BY RAND() LIMIT 1) AS user_name,
    (SELECT user_id FROM `users` ORDER BY RAND() LIMIT 1) AS assigned_to,
    (SELECT project_name FROM `projects` ORDER BY RAND() LIMIT 1) AS project_name
FROM
    (SELECT 1 AS id UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4 UNION ALL SELECT 5 UNION ALL SELECT 6 UNION ALL SELECT 7 UNION ALL SELECT 8 UNION ALL SELECT 9 UNION ALL SELECT 10) AS dummy;

INSERT INTO `user_assignment` (user_id, task_id) VALUES (9, 2);
INSERT INTO `user_assignment` (user_id, task_id) VALUES (10, 4);
INSERT INTO `user_assignment` (user_id, task_id) VALUES (12, 3);
INSERT INTO `user_assignment` (user_id, task_id) VALUES (18, 4);
INSERT INTO `user_assignment` (user_id, task_id) VALUES (10, 5);
INSERT INTO `user_assignment` (user_id, task_id) VALUES (14, 9);
INSERT INTO `user_assignment` (user_id, task_id) VALUES (14, 10);
INSERT INTO `user_assignment` (user_id, task_id) VALUES (15, 7);
INSERT INTO `user_assignment` (user_id, task_id) VALUES (17, 9);
INSERT INTO `user_assignment` (user_id, task_id) VALUES (10, 6);

INSERT INTO `pull_request_assignments` (user_id, pull_request_id) VALUES (9, 2);
INSERT INTO `pull_request_assignments` (user_id, pull_request_id) VALUES (10, 4);
INSERT INTO `pull_request_assignments` (user_id, pull_request_id) VALUES (12, 3);
INSERT INTO `pull_request_assignments` (user_id, pull_request_id) VALUES (18, 4);
INSERT INTO `pull_request_assignments` (user_id, pull_request_id) VALUES (10, 5);
INSERT INTO `pull_request_assignments` (user_id, pull_request_id) VALUES (14, 9);
INSERT INTO `pull_request_assignments` (user_id, pull_request_id) VALUES (14, 10);
INSERT INTO `pull_request_assignments` (user_id, pull_request_id) VALUES (15, 7);
INSERT INTO `pull_request_assignments` (user_id, pull_request_id) VALUES (17, 9);
INSERT INTO `pull_request_assignments` (user_id, pull_request_id) VALUES (10, 6);

-- Insert random data into `programming_languages` table

INSERT INTO `programming_languages` (language, project_id) VALUES ("java", 1);
INSERT INTO `programming_languages` (language, project_id) VALUES ("html", 2);
INSERT INTO `programming_languages` (language, project_id) VALUES ("javascript", 3);
INSERT INTO `programming_languages` (language, project_id) VALUES ("php", 4);
INSERT INTO `programming_languages` (language, project_id) VALUES ("css", 5);
INSERT INTO `programming_languages` (language, project_id) VALUES ("sql", 6);
INSERT INTO `programming_languages` (language, project_id) VALUES ("c", 7);
INSERT INTO `programming_languages` (language, project_id) VALUES ("c#", 8);
INSERT INTO `programming_languages` (language, project_id) VALUES ("java", 9);
INSERT INTO `programming_languages` (language, project_id) VALUES ("python", 10);