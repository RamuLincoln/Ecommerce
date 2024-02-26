CREATE DATABASE  IF NOT EXISTS `furniture` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `furniture`;
-- MySQL dump 10.13  Distrib 8.0.27, for macos11 (x86_64)
--
-- Host: localhost    Database: furniture
-- ------------------------------------------------------
-- Server version	8.0.27

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
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category` (
  `categoryid` int NOT NULL AUTO_INCREMENT,
  `categoryname` varchar(45) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `is_active` bit(1) NOT NULL DEFAULT b'1',
  `image` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`categoryid`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (1,'table',NULL,_binary '','https://image.zanui.com.au/data/simple/44/1633/698513.jpg'),(2,'sofa',NULL,_binary '','https://images.demandware.net/dw/image/v2/BBBV_PRD/on/demandware.static/-/Sites-master-catalog/default/dwd633af54/images/700000/704909.jpg?sfrm=jpg'),(3,'chair','Both indoor and outdoor',_binary '','https://www.fantasticfurniture.com.au/medias/LYOCHA1STOOOMEFGRY-PD-1-CONTAINER-original-FantasticFurniture-WF-Product-Detail?context=bWFzdGVyfGltYWdlc3wxNTI1N3xpbWFnZS9qcGVnfGg0YS9oNzcvOTQ1NDU3NDQ2OTE1MC9MWU9DSEExU1RPT09NRUZHUllfUERfMV9DT05UQUlORVJfb3JpZ2luYWxfRmFudGFzdGljRnVybml0dXJlLVdGX1Byb2R1Y3QtRGV0YWlsfGEyYmE1N2FhOWNiN2YzMTM1M2EyNjJjMjZiYzliMTIxZmZiM2JiN2JkYmIwMjNkNTFmMTg2YmRkOWY2MjI0MGE'),(4,'bed','Frame Only',_binary '','https://www.ikea.com/om/en/images/products/slattum-upholstered-bed-frame-knisa-light-grey__0726726_pe735401_s5.jpg?f=s');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `customerid` int NOT NULL AUTO_INCREMENT,
  `firstname` varchar(45) DEFAULT NULL,
  `lastname` varchar(45) DEFAULT NULL,
  `DOB` varchar(25) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `address` varchar(45) DEFAULT NULL,
  `joindate` varchar(20) DEFAULT NULL,
  `is_active` varchar(5) NOT NULL DEFAULT '',
  PRIMARY KEY (`customerid`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'Alan','Walker','01-03-1978','0220116789','alan@gmail.com','12 Ken Street','02-02-2022','1'),(2,'Christine','Mistry','02-03-1993','0220908778','christine@gmail.com','33 Ben Ave','02-03-2021','0'),(3,'Mini','Rohde','1983-01-09','02201298183','mini@gmail.com','24 Kilmore Street','03-09-2022','1'),(4,'Trisha','Packer','1990-09-01','0220119093','trisha@gmail.com','12 lincoln road','03-03-2022','1'),(5,'Sam','Newton','1978-09-10','02203301938','sam@gmail.com','5 view road ','09-10-2022','1'),(6,'Denise','Lum','1978-01-09','02498392301','denise@gmail.com','111 new south road','09-10-2022','1'),(7,'Andrea','Browne','1978-09-10','02102789029','andrea@gmail.com','90 Quay Street','09-10-2022','1'),(8,'Sarah','Toia','1978-03-20','02102304913','sarah@gmail.com','11 Beach road','10-10-2022','1'),(9,'Monique','Stong','1965-10-09','02201903941','monique@gmail.com','90 Central Road','02-10-2022','1'),(10,'Taylor','Suyat','1991-01-01','02100019384','taylor@gmail.com','56 Key Street','01-01-2022','1'),(15,'Ramond','Rami','1991-03-02','02102234567','awesome@example.com','01 Caledonian Road',NULL,'1'),(16,'Ramu','Tania','1991-09-09','02102202938','ramu@gmail.com','45 mountain road','02-03-2022','1');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `furniture`
--

DROP TABLE IF EXISTS `furniture`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `furniture` (
  `furnitureid` int NOT NULL AUTO_INCREMENT,
  `furniturename` varchar(50) DEFAULT NULL,
  `categoryid` int DEFAULT NULL,
  `refurbishid` int DEFAULT NULL,
  `sellerid` int DEFAULT NULL,
  `staffid` int DEFAULT NULL,
  `purchasedprice` int DEFAULT NULL,
  `sellprice` int DEFAULT NULL,
  `discount` varchar(15) DEFAULT NULL,
  `periodofdiscount` datetime DEFAULT NULL,
  `description` varchar(1000) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  `purchaseddate` varchar(20) DEFAULT NULL,
  `purchasestatus` varchar(25) DEFAULT NULL,
  `is_active` varchar(5) NOT NULL DEFAULT '',
  `image` varchar(1000) DEFAULT NULL,
  `customerid` int DEFAULT NULL,
  `bargainPrice` int DEFAULT NULL,
  PRIMARY KEY (`furnitureid`),
  KEY `category_idx` (`categoryid`),
  KEY `refurbish_idx` (`refurbishid`),
  KEY `seller_idx` (`sellerid`),
  KEY `stafid_idx` (`staffid`),
  KEY `staffid_idx` (`staffid`),
  CONSTRAINT `category` FOREIGN KEY (`categoryid`) REFERENCES `category` (`categoryid`),
  CONSTRAINT `refurbish` FOREIGN KEY (`refurbishid`) REFERENCES `refurbishment` (`refurbishid`),
  CONSTRAINT `seller` FOREIGN KEY (`sellerid`) REFERENCES `seller` (`sellerid`),
  CONSTRAINT `staffid` FOREIGN KEY (`staffid`) REFERENCES `furniture` (`furnitureid`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `furniture`
--

LOCK TABLES `furniture` WRITE;
/*!40000 ALTER TABLE `furniture` DISABLE KEYS */;
INSERT INTO `furniture` VALUES (1,'Accent Roud Coffee Table',1,1,1,1,70,300,'270','2022-10-17 00:00:00','Width: 120cm, Length: 75cm, height 73cm','sold','03-07-2022','Accept','0','https://cdn.shopify.com/s/files/1/0529/3749/0582/products/ClassicCoffeeTable-BxSS_966x966.jpg?v=1645081289',1,NULL),(2,'Umbra Bell Wood Table',1,2,2,1,200,600,'500','2022-10-21 00:00:00','Width:50, Length: 75cm, height: 75cm, color white ','completed','01-09-2022',NULL,'1','https://themarket.azureedge.net/resizer/view?key=05ca673fdd01ddcfb508d773a6c7672e&b=productimages&w=418&h=632',15,NULL),(3,'Lolo Coffee table',1,3,3,1,100,350,'315','2022-10-20 00:00:00','two sizes 600D and 800D','sold','10-09-2022',NULL,'0','https://themarket.azureedge.net/resizer/view?key=4c06e83b4e78bd2d75f8565c79712329&b=productimages&w=418&h=632',16,NULL),(4,'Ergoplan table',1,4,3,1,150,500,'450','2022-10-27 00:00:00','Wood: Solid Pine  Color: Natural Size: 1300x700x430','sold','03-09-2022',NULL,'0','https://cdn.shopify.com/s/files/1/0019/6250/8351/products/knight-ergoplan-coffee-table-1200mm-x-600mm-tawa-2618964246591_x700.jpg?v=1570391874',2,NULL),(5,'Barberra Boucle Armchair',2,5,4,1,300,750,'570','2022-10-21 00:00:00','colour: moss green boucle dimensions: width 59, depth 84, height 83cm','completed','01-09-2022',NULL,'1','https://themarket.azureedge.net/resizer/view?key=77535c473aebbbc0c6a1442682545cc0&b=productimages&w=418&h=632',3,NULL),(6,'AMBERLEY FABRIC SOFA (GREY)',2,6,5,1,400,950,'855','2022-10-22 00:00:00','grey colour, tiles and button tufted design, linen fabric','on sale','23-09-2022',NULL,'1','https://www.ifurniture.co.nz/images/thumbs/0046650_amberley-fabric-sofa-grey-32-set.jpeg',4,NULL),(7,'Anabella Sofa',2,7,5,1,300,750,'600','2022-11-01 00:00:00','Solid wood legs. Overall 37\'\' H x 84.5\'\' W x 36.5\'\' D','on sale','03-08-2022',NULL,'1','https://www.homecarechairs.co.uk/wp-content/uploads/2016/12/s29web-800x800.jpg',5,NULL),(8,'Apollo Sofa',2,8,6,1,700,1300,NULL,NULL,'Individual 1 Seater Dimensions : 85.0 cm x 85.0 cm x 91.0 cm','completed','15-09-2022',NULL,'1','https://www.ulcdn.net/images/products/94259/original/Apollo_Infinite_FNSF51APDU30000SAAAA_slide_00.jpg?1467963845',6,NULL),(9,'Sesame Armchair',3,9,7,1,150,350,'320','2022-10-30 00:00:00','Slate grey fabric, Natural wooden arms and legs, 5-year warranty. ','on sale','01-09-2022',NULL,'1','https://danskemobler.co.nz/images/products/large/2217_Sesame%20Arm%20Chair%20-%20angle%20RET.jpg',7,NULL),(10,'Amsteardam sofa',2,10,8,1,400,900,NULL,NULL,'Stone Estoril leather, matte dark grey, seats 3','on sale','01-09-2022',NULL,'1','https://images.demandware.net/dw/image/v2/BBBV_PRD/on/demandware.static/-/Sites-master-catalog/default/dw901c9b2a/images/750000/751247.jpg?sw=2000',8,NULL),(11,'Lerhamn Chair',3,11,8,1,100,400,NULL,NULL,'The chair frame is made of solid wood, which is a durable natural material.','on sale','12-09-2022',NULL,'1','https://www.ikea.com/us/en/images/products/lerhamn-chair-black-brown-vittaryd-beige__0728160_pe736117_s5.jpg?f=xl',8,NULL),(12,'Pello Chair',3,12,9,1,200,700,NULL,NULL,'PELLO armchair has a bent shape that is slightly resilient when you’re seated and provides comfortable back and neck support.','on sale','01-09-2022',NULL,'1','http://cdn.shopify.com/s/files/1/0023/6932/3072/products/pello-armchair__38296_PE130209_S5.jpg?v=1586661211',10,NULL),(13,'Malm Bed Frame',4,13,4,1,200,550,NULL,NULL,'Ample storage space is hidden neatly under the bed in 2 large drawers. Perfect for storing quilts, pillows and bed linen.','on sale','20-08-2022',NULL,'1','https://www.ikea.com/us/en/images/products/malm-high-bed-frame-2-storage-boxes-black-brown-luroey__0637597_pe698414_s5.jpg?f=xl',2,NULL),(14,'HEMNES Frame',4,14,10,1,150,550,'450','2022-10-25 00:00:00','The high footboard keeps bed textiles from falling onto the floor while you sleep.','on sale','24-08-2022',NULL,'1','https://www.ikea.com/us/en/images/products/hemnes-bed-frame-white-stain-luroey__0637516_pe698353_s5.jpg?f=xs',5,NULL),(15,'TRAVA Frame',4,15,10,2,150,490,'400','2022-10-21 00:00:00','TARVA bed frame is a modern example of Scandinavian furniture tradition – a simple design and untreated wood. A timeless expression mixes nicely with a variety of other styles and furniture.','on sale','29-08-2022',NULL,'1','https://www.ikea.com/us/en/images/products/tarva-bed-frame-pine-luroey__0637611_pe698421_s5.jpg?f=xs',4,NULL),(24,'Sofa Red',2,24,NULL,1,300,750,'675','2022-10-15 00:00:00','in good condition','on sale','08-10-2022','Accept','0','/static/images/22ddcb51-abb7-4027-85fd-93761bc68eef.webp',7,NULL),(32,'Oakley Dining Table',1,32,NULL,1,200,500,'450','2022-10-28 00:00:00','Indoor table','on sale','2022-10-17','Accept','1','https://danskemobler.co.nz/images/products/main/2985_Oakley%20Dining%20Table%20-%20front%20on.jpg',1,200),(33,'Mara White Marble Table',1,33,NULL,1,500,700,NULL,NULL,'14mm solid white sealed marble Solid Oak legs with a Walnut stain Round shape','on sale','2022-10-20','Accept','1','/static/images/e7d379af-6555-4b5b-a0c6-fb75640f712c.jpeg',4,NULL),(34,'Raynor round table',1,34,NULL,1,300,500,NULL,NULL,'MDF, solid American white oak, American white oak veneer, Solid beech legs','on sale','2022-10-20','Accept','1','/static/images/4ded8a09-1211-4418-8169-b47e0e574ec1.jpeg',6,NULL),(35,'NODELAND table',1,35,NULL,1,250,600,'500','2022-10-26 00:00:00','medium white, 80x50 cm (31 1/2x19 5/8 \")','on sale','2022-10-20','Accept','1','/static/images/36d11eb5-6521-4bec-aebe-58cb8e9f4c1b.jpeg',8,NULL);
/*!40000 ALTER TABLE `furniture` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order`
--

DROP TABLE IF EXISTS `order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order` (
  `orderid` int NOT NULL AUTO_INCREMENT,
  `customerid` int DEFAULT NULL,
  `deliverystatus` varchar(20) DEFAULT NULL,
  `estimatedarrivaltime` varchar(20) DEFAULT NULL,
  `deliveryaddress` varchar(45) DEFAULT NULL,
  `orderdate` varchar(20) DEFAULT NULL,
  `review` varchar(100) DEFAULT NULL,
  `furnitureid` int DEFAULT NULL,
  `price` int DEFAULT NULL,
  PRIMARY KEY (`orderid`),
  KEY `order_customer_null_fk` (`customerid`),
  KEY `order_furniture_null_fk` (`furnitureid`),
  CONSTRAINT `order_customer_null_fk` FOREIGN KEY (`customerid`) REFERENCES `customer` (`customerid`),
  CONSTRAINT `order_furniture_null_fk` FOREIGN KEY (`furnitureid`) REFERENCES `furniture` (`furnitureid`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order`
--

LOCK TABLES `order` WRITE;
/*!40000 ALTER TABLE `order` DISABLE KEYS */;
INSERT INTO `order` VALUES (1,2,'delivered','03-09-2022','33 Mountain View Road','25-08-2022','good service',1,270),(2,1,'delivered','10-10-2022','27 Kauri Road','13-09-2022',NULL,3,315),(39,1,'processing','2022-10-13','12 Ken Street','2022-10-10',NULL,4,450);
/*!40000 ALTER TABLE `order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payment`
--

DROP TABLE IF EXISTS `payment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payment` (
  `paymentid` int NOT NULL AUTO_INCREMENT,
  `orderid` int DEFAULT NULL,
  `totalamount` int DEFAULT NULL,
  PRIMARY KEY (`paymentid`),
  KEY `order_idx` (`orderid`),
  CONSTRAINT `order` FOREIGN KEY (`orderid`) REFERENCES `order` (`orderid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payment`
--

LOCK TABLES `payment` WRITE;
/*!40000 ALTER TABLE `payment` DISABLE KEYS */;
INSERT INTO `payment` VALUES (1,1,300);
/*!40000 ALTER TABLE `payment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `refurbishment`
--

DROP TABLE IF EXISTS `refurbishment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `refurbishment` (
  `refurbishid` int NOT NULL AUTO_INCREMENT,
  `staffid` int DEFAULT NULL,
  `refurbishdate` varchar(20) DEFAULT NULL,
  `cost` int DEFAULT NULL,
  `status` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`refurbishid`),
  KEY `staff_idx` (`staffid`),
  KEY `staf_idx` (`staffid`),
  CONSTRAINT `staf` FOREIGN KEY (`staffid`) REFERENCES `refurbishment` (`refurbishid`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `refurbishment`
--

LOCK TABLES `refurbishment` WRITE;
/*!40000 ALTER TABLE `refurbishment` DISABLE KEYS */;
INSERT INTO `refurbishment` VALUES (1,1,'01-08-2022',100,'completed'),(2,1,'09-09-2022',100,'completed'),(3,1,'20-09-2022',100,'completed'),(4,1,'15-09-2022',200,'completed'),(5,1,'10-09-2022',100,'completed'),(6,1,'30-09-2022',250,'completed'),(7,1,'01-09-2022',NULL,'completed'),(8,1,'28-09-2022',NULL,'completed'),(9,1,'16-09-2022',NULL,'completed'),(10,1,'13-09-2022',200,'completed'),(11,1,'20-09-2022',150,'completed'),(12,1,'13-09-2022',300,'completed'),(13,1,'19-07-2022',200,'completed'),(14,1,'02-09-2022',30,'completed'),(15,2,'09-09-2022',200,NULL),(24,NULL,NULL,NULL,NULL),(25,NULL,NULL,NULL,NULL),(26,NULL,NULL,NULL,NULL),(27,NULL,NULL,NULL,NULL),(28,NULL,NULL,NULL,NULL),(29,NULL,NULL,NULL,NULL),(30,NULL,NULL,NULL,NULL),(31,NULL,NULL,NULL,NULL),(32,NULL,NULL,100,NULL),(33,NULL,NULL,NULL,NULL),(34,NULL,NULL,NULL,NULL),(35,NULL,NULL,100,NULL);
/*!40000 ALTER TABLE `refurbishment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `requests`
--

DROP TABLE IF EXISTS `requests`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `requests` (
  `id` int NOT NULL AUTO_INCREMENT,
  `customerid` int DEFAULT NULL,
  `staffid` int DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `category` varchar(50) DEFAULT NULL,
  `furniturename` varchar(50) DEFAULT NULL,
  `response` varchar(100) DEFAULT NULL,
  `requestdate` varchar(20) DEFAULT NULL,
  `reponsedate` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `customer_idx` (`customerid`),
  KEY `staff_idx` (`staffid`),
  CONSTRAINT `customer` FOREIGN KEY (`customerid`) REFERENCES `customer` (`customerid`),
  CONSTRAINT `staff` FOREIGN KEY (`staffid`) REFERENCES `staff` (`staffid`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `requests`
--

LOCK TABLES `requests` WRITE;
/*!40000 ALTER TABLE `requests` DISABLE KEYS */;
INSERT INTO `requests` VALUES (1,1,1,'Round coffee table','table','wood table','We dont have it in stock','2022-10-07','2022-10-17'),(4,1,NULL,'A blue chair with white pattern','Chair','game Chair','We dont have game chair in stock','2022-10-07','2022-10-16'),(6,1,NULL,'Width:, Length: 75cm, height: 75cm, color white ','sofa','red sofa','we dont have it in stock','2022-10-16','2022-10-17'),(7,1,NULL,'large indoor sofa in red color','sofa','red sofa','we have it in stock','2022-10-17','2022-10-17');
/*!40000 ALTER TABLE `requests` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `review`
--

DROP TABLE IF EXISTS `review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `review` (
  `id` int NOT NULL AUTO_INCREMENT,
  `customerid` int DEFAULT NULL,
  `staffid` int DEFAULT NULL,
  `orderid` int DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `staffreply` varchar(100) DEFAULT NULL,
  `rating` varchar(45) DEFAULT NULL,
  `furniturename` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `cus_idx` (`customerid`),
  KEY `staf_idx` (`staffid`),
  KEY `oder_idx` (`orderid`),
  KEY `customercustomer_idx` (`customerid`),
  KEY `furname_idx` (`furniturename`),
  KEY `fname_idx` (`furniturename`),
  KEY `furnitureName_idx` (`furniturename`),
  CONSTRAINT `customercustomer` FOREIGN KEY (`customerid`) REFERENCES `customer` (`customerid`),
  CONSTRAINT `orderoder` FOREIGN KEY (`orderid`) REFERENCES `order` (`orderid`),
  CONSTRAINT `statffstaff` FOREIGN KEY (`staffid`) REFERENCES `staff` (`staffid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `review`
--

LOCK TABLES `review` WRITE;
/*!40000 ALTER TABLE `review` DISABLE KEYS */;
INSERT INTO `review` VALUES (1,1,1,2,NULL,NULL,NULL,NULL),(2,2,1,1,NULL,NULL,NULL,NULL),(4,1,NULL,2,'Good',NULL,'3',NULL);
/*!40000 ALTER TABLE `review` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `seller`
--

DROP TABLE IF EXISTS `seller`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `seller` (
  `sellerid` int NOT NULL AUTO_INCREMENT,
  `firstname` varchar(45) DEFAULT NULL,
  `lastname` varchar(45) DEFAULT NULL,
  `DOB` varchar(25) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `address` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`sellerid`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `seller`
--

LOCK TABLES `seller` WRITE;
/*!40000 ALTER TABLE `seller` DISABLE KEYS */;
INSERT INTO `seller` VALUES (1,'Margaret','Wilson','01-02-1983','0220119009','32 Lincoln Road','margaret11@hotmail.com'),(2,'Kristy','Lasir','09-08-1973','021008990','78 Broad Road','kristy@gmail.com'),(3,'Gonzalo','Valdez','09-09-1962','02109098670','31 Quey Street','gonzalo@gmail.com'),(4,'Maria','Doan','01-02-1988','02293809647','98 Ken Road','maria@gmail.com'),(5,'Atunaisa','Begg','09-10-1982','02198901936','99 Kings Road','atunaisa@gmail.com'),(6,'Adi','Armstrong','03-02-1991','02201938401','77 Rail Road','adi@gmail.com'),(7,'Susana','Ratu','09-10-1990','02109319038','8 Gail Ave','susana@gmail.com'),(8,'Naomi','Park','13-09-1981','02201938918','29 Carls Street','naomi@gmail.com'),(9,'Wallace','Koning','25-09-1971','02209117042','23 Apolo Road','wallace@gmail.com'),(10,'Danielle','Low Chee','23-06-1953','02198903812','30 Holly Road',NULL);
/*!40000 ALTER TABLE `seller` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shoppingcart`
--

DROP TABLE IF EXISTS `shoppingcart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shoppingcart` (
  `cartid` int NOT NULL AUTO_INCREMENT,
  `furnitureid` int DEFAULT NULL,
  `customerid` int DEFAULT NULL,
  `quantity` varchar(10) DEFAULT NULL,
  `totalamount` int DEFAULT NULL,
  PRIMARY KEY (`cartid`),
  KEY `cux_idx` (`customerid`),
  KEY `fur_idx` (`furnitureid`),
  CONSTRAINT `cux` FOREIGN KEY (`customerid`) REFERENCES `customer` (`customerid`),
  CONSTRAINT `fur` FOREIGN KEY (`furnitureid`) REFERENCES `furniture` (`furnitureid`)
) ENGINE=InnoDB AUTO_INCREMENT=96 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shoppingcart`
--

LOCK TABLES `shoppingcart` WRITE;
/*!40000 ALTER TABLE `shoppingcart` DISABLE KEYS */;
INSERT INTO `shoppingcart` VALUES (53,2,16,'1',600),(60,7,15,'1',750),(61,5,15,'1',750),(62,6,15,'1',950),(66,24,5,'1',750),(93,9,1,'1',350);
/*!40000 ALTER TABLE `shoppingcart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staff`
--

DROP TABLE IF EXISTS `staff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `staff` (
  `staffid` int NOT NULL AUTO_INCREMENT,
  `firstname` varchar(45) DEFAULT NULL,
  `lastname` varchar(45) DEFAULT NULL,
  `DOB` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `address` varchar(45) DEFAULT NULL,
  `is_active` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`staffid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff`
--

LOCK TABLES `staff` WRITE;
/*!40000 ALTER TABLE `staff` DISABLE KEYS */;
INSERT INTO `staff` VALUES (1,'Keiran','Harmey','03-09-1975','keiran@gmail.com','33 Sally Road','1');
/*!40000 ALTER TABLE `staff` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-10-20 22:40:21
