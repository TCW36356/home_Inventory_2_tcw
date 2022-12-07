SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

USE `home_inventory`;

INSERT INTO `items` (item, count, inventory_id) values('LEGO Set', 5, 1);
INSERT INTO `items` (item, count, inventory_id) values('MacBook Pro', 1, 1);
INSERT INTO `items` (item, count, inventory_id) values('Table', 1, 1);
INSERT INTO `items` (item, count, inventory_id) values('Car', 1, 1);
INSERT INTO `items` (item, count, inventory_id) values('Chair', 1, 1);
INSERT INTO `items` (item, count, inventory_id) values('Bookcase', 6, 1);
INSERT INTO `items` (item, count, inventory_id) values('Couch', 1, 1);




COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;