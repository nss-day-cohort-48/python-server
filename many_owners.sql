Create Table CustomerAnimal (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `customer_id` INTEGER NOT NULL,
    `animal_id` INTEGER NOT NULL,
    FOREIGN KEY(`customer_id`) REFERENCES `Customer`(`id`),
    FOREIGN KEY(`animal_id`) REFERENCES `Animal`(`id`)
);

DROP TABLE Animal;

CREATE TABLE `Animal` (
	`id`  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name`  TEXT NOT NULL,
	`status` TEXT NOT NULL,
	`breed` TEXT NOT NULL,
	`location_id` INTEGER,
	FOREIGN KEY(`location_id`) REFERENCES `Location`(`id`)
);

INSERT INTO `Animal` VALUES (null, "Snickers", "Recreation", "Dalmation", 1);
INSERT INTO `Animal` VALUES (null, "Jax", "Treatment", "Beagle", 1);
INSERT INTO `Animal` VALUES (null, "Falafel", "Treatment", "Siamese", 2);
INSERT INTO `Animal` VALUES (null, "Doodles", "Kennel", "Poodle", 1);
INSERT INTO `Animal` VALUES (null, "Daps", "Kennel", "Boxer", 2);
INSERT INTO `Customer` VALUES (null, "Scott Silver", "454 Mulberry Way", "scott@silver.com", "password");



INSERT INTO `CustomerAnimal` VALUES (null, 4, 1);
INSERT INTO `CustomerAnimal` VALUES (null, 5, 1);
INSERT INTO `CustomerAnimal` VALUES (null, 1, 2);
INSERT INTO `CustomerAnimal` VALUES (null, 4, 3);
INSERT INTO `CustomerAnimal` VALUES (null, 5, 3);
INSERT INTO `CustomerAnimal` VALUES (null, 3, 4);
INSERT INTO `CustomerAnimal` VALUES (null, 2, 5);

Select
    c.id,
    c.name
From Customer c
Join CustomerAnimal ca on c.id = ca.customer_id
Join Animal a on a.id = ca.animal_id
where a.id = 1;
