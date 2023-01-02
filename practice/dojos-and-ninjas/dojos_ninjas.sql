-- MySQL dump 10.13  Distrib 8.0.22, for macos10.15 (x86_64)
--
-- Host: localhost    Database: dojos_ninjas
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `dojos`
--

DROP TABLE IF EXISTS `dojos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dojos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(225) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dojos`
--

LOCK TABLES `dojos` WRITE;
/*!40000 ALTER TABLE `dojos` DISABLE KEYS */;
INSERT INTO `dojos` VALUES (1,'San Francisco','2022-07-16 12:36:04','2022-07-16 12:36:04'),(2,'San Jose','2022-07-16 12:36:04','2022-07-16 12:36:04'),(3,'Seatlle','2022-07-16 12:36:04','2022-07-16 12:36:04'),(4,'Chicago','2022-07-16 12:36:04','2022-07-16 12:36:04'),(5,'Burbank','2022-07-16 14:58:06','2022-07-16 14:58:06'),(6,'Arizona','2022-07-16 15:00:27','2022-07-16 15:00:27'),(7,'Colorado','2022-07-16 15:26:07','2022-07-16 15:26:07'),(8,'New York','2022-07-16 16:09:06','2022-07-16 16:09:06');
/*!40000 ALTER TABLE `dojos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ninjas`
--

DROP TABLE IF EXISTS `ninjas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ninjas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) DEFAULT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  `age` int DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `dojos_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_ninjas_dojos_idx` (`dojos_id`),
  CONSTRAINT `fk_ninjas_dojos` FOREIGN KEY (`dojos_id`) REFERENCES `dojos` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ninjas`
--

LOCK TABLES `ninjas` WRITE;
/*!40000 ALTER TABLE `ninjas` DISABLE KEYS */;
INSERT INTO `ninjas` VALUES (1,'Jacob','Truong',26,'2022-07-16 13:38:26','2022-07-16 13:38:26',2),(2,'Jacob','Truong',26,'2022-07-16 13:49:42','2022-07-16 13:49:42',2),(3,'Jacob','Truong',26,'2022-07-16 13:49:52','2022-07-16 13:49:52',2),(4,'Andrew','Peck',30,'2022-07-16 14:09:20','2022-07-16 14:09:20',3),(5,'Andrew','Peck',30,'2022-07-16 14:09:44','2022-07-16 14:09:44',3),(6,'Andrew','Peck',30,'2022-07-16 14:10:21','2022-07-16 14:10:21',3),(7,'Andrew','Peck',30,'2022-07-16 14:10:44','2022-07-16 14:10:44',3),(8,'Andrew','Peck',30,'2022-07-16 14:11:02','2022-07-16 14:11:02',3),(9,'Andrew','Peck',30,'2022-07-16 14:14:20','2022-07-16 14:14:20',3),(10,'Andrew','Peck',30,'2022-07-16 14:15:15','2022-07-16 14:15:15',3),(11,'Andrew','Peck',30,'2022-07-16 14:20:19','2022-07-16 14:20:19',3),(12,'Andrew','Peck',30,'2022-07-16 14:21:01','2022-07-16 14:21:01',3),(13,'Andrew','Peck',30,'2022-07-16 14:22:22','2022-07-16 14:22:22',3),(14,'Andrew','Peck',30,'2022-07-16 14:22:40','2022-07-16 14:22:40',3),(15,'Andrew','Peck',30,'2022-07-16 14:22:50','2022-07-16 14:22:50',3),(16,'Andrew','Peck',30,'2022-07-16 14:24:16','2022-07-16 14:24:16',3),(17,'Andrew','Peck',30,'2022-07-16 14:24:28','2022-07-16 14:24:28',3),(18,'Andrew','Peck',30,'2022-07-16 14:24:37','2022-07-16 14:24:37',3),(19,'Andrew','Peck',30,'2022-07-16 14:24:47','2022-07-16 14:24:47',3),(20,'Andrew','Peck',30,'2022-07-16 14:25:01','2022-07-16 14:25:01',3),(21,'Andrew','Peck',30,'2022-07-16 14:25:08','2022-07-16 14:25:08',3),(22,'Andrew','Peck',30,'2022-07-16 14:25:17','2022-07-16 14:25:17',3),(23,'Andrew','Peck',30,'2022-07-16 14:25:29','2022-07-16 14:25:29',3),(24,'Kim','Kardashian',40,'2022-07-16 15:17:02','2022-07-16 15:17:02',5),(25,'Sonny','Chhuon',32,'2022-07-16 15:23:40','2022-07-16 15:23:40',3),(26,'Sonny','Chhuon',32,'2022-07-16 15:25:25','2022-07-16 15:25:25',3),(27,'Sonny','Chhuon',32,'2022-07-16 15:25:48','2022-07-16 15:25:48',3);
/*!40000 ALTER TABLE `ninjas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-07-16 18:54:52
