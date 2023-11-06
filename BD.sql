CREATE DATABASE  IF NOT EXISTS `papeleria` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `papeleria`;
-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: papeleria
-- ------------------------------------------------------
-- Server version	8.0.32

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add categoria',7,'add_categoria'),(26,'Can change categoria',7,'change_categoria'),(27,'Can delete categoria',7,'delete_categoria'),(28,'Can view categoria',7,'view_categoria'),(29,'Can add cliente',8,'add_cliente'),(30,'Can change cliente',8,'change_cliente'),(31,'Can delete cliente',8,'delete_cliente'),(32,'Can view cliente',8,'view_cliente'),(33,'Can add proveedor',9,'add_proveedor'),(34,'Can change proveedor',9,'change_proveedor'),(35,'Can delete proveedor',9,'delete_proveedor'),(36,'Can view proveedor',9,'view_proveedor'),(37,'Can add producto',10,'add_producto'),(38,'Can change producto',10,'change_producto'),(39,'Can delete producto',10,'delete_producto'),(40,'Can view producto',10,'view_producto'),(41,'Can add pedido',11,'add_pedido'),(42,'Can change pedido',11,'change_pedido'),(43,'Can delete pedido',11,'delete_pedido'),(44,'Can view pedido',11,'view_pedido'),(45,'Can add movimiento producto',12,'add_movimientoproducto'),(46,'Can change movimiento producto',12,'change_movimientoproducto'),(47,'Can delete movimiento producto',12,'delete_movimientoproducto'),(48,'Can view movimiento producto',12,'view_movimientoproducto'),(49,'Can add factura',13,'add_factura'),(50,'Can change factura',13,'change_factura'),(51,'Can delete factura',13,'delete_factura'),(52,'Can view factura',13,'view_factura');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(7,'Papeleria','categoria'),(8,'Papeleria','cliente'),(13,'Papeleria','factura'),(12,'Papeleria','movimientoproducto'),(11,'Papeleria','pedido'),(10,'Papeleria','producto'),(9,'Papeleria','proveedor'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'Papeleria','0001_initial','2023-11-05 19:05:19.873649'),(2,'Papeleria','0002_auto_20231101_1802','2023-11-05 19:05:20.135234'),(3,'Papeleria','0003_auto_20231105_1405','2023-11-05 19:05:20.368778'),(4,'contenttypes','0001_initial','2023-11-05 19:05:20.581130'),(5,'auth','0001_initial','2023-11-05 19:05:23.081842'),(6,'admin','0001_initial','2023-11-05 19:05:23.851151'),(7,'admin','0002_logentry_remove_auto_add','2023-11-05 19:05:23.890862'),(8,'admin','0003_logentry_add_action_flag_choices','2023-11-05 19:05:23.926104'),(9,'contenttypes','0002_remove_content_type_name','2023-11-05 19:05:24.257126'),(10,'auth','0002_alter_permission_name_max_length','2023-11-05 19:05:24.449741'),(11,'auth','0003_alter_user_email_max_length','2023-11-05 19:05:24.528772'),(12,'auth','0004_alter_user_username_opts','2023-11-05 19:05:24.570666'),(13,'auth','0005_alter_user_last_login_null','2023-11-05 19:05:24.747569'),(14,'auth','0006_require_contenttypes_0002','2023-11-05 19:05:24.776767'),(15,'auth','0007_alter_validators_add_error_messages','2023-11-05 19:05:24.824292'),(16,'auth','0008_alter_user_username_max_length','2023-11-05 19:05:25.041184'),(17,'auth','0009_alter_user_last_name_max_length','2023-11-05 19:05:25.318411'),(18,'auth','0010_alter_group_name_max_length','2023-11-05 19:05:25.419610'),(19,'auth','0011_update_proxy_permissions','2023-11-05 19:05:25.519122'),(20,'auth','0012_alter_user_first_name_max_length','2023-11-05 19:05:25.736655'),(21,'sessions','0001_initial','2023-11-05 19:05:25.946875'),(22,'Papeleria','0004_auto_20231105_1426','2023-11-05 19:26:34.918274');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `papeleria_categoria`
--

DROP TABLE IF EXISTS `papeleria_categoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `papeleria_categoria` (
  `ID_CATEGORIA` int NOT NULL AUTO_INCREMENT,
  `DESCRIPCION_CATEGORIA` varchar(30) NOT NULL,
  `ESTADO_PRODUCTO` varchar(1) NOT NULL,
  PRIMARY KEY (`ID_CATEGORIA`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `papeleria_categoria`
--

LOCK TABLES `papeleria_categoria` WRITE;
/*!40000 ALTER TABLE `papeleria_categoria` DISABLE KEYS */;
INSERT INTO `papeleria_categoria` VALUES (1,'Juguete','A'),(2,'Cuaderno','A'),(3,'Papel','A');
/*!40000 ALTER TABLE `papeleria_categoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `papeleria_cliente`
--

DROP TABLE IF EXISTS `papeleria_cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `papeleria_cliente` (
  `ID_CLIENTE` int NOT NULL AUTO_INCREMENT,
  `NOMBRE_CLIENTE` varchar(30) NOT NULL,
  `APELLIDO_CLIENTE` varchar(30) NOT NULL,
  `DIRECCION_CLIENTE` varchar(30) NOT NULL,
  `TELEFONO_CLIENTE` varchar(30) NOT NULL,
  `CORREO_CLIENTE` varchar(30) NOT NULL,
  PRIMARY KEY (`ID_CLIENTE`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `papeleria_cliente`
--

LOCK TABLES `papeleria_cliente` WRITE;
/*!40000 ALTER TABLE `papeleria_cliente` DISABLE KEYS */;
INSERT INTO `papeleria_cliente` VALUES (1,'Jose','Jimenez','cra 26','3920193842','jose@gmail.com');
/*!40000 ALTER TABLE `papeleria_cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `papeleria_factura`
--

DROP TABLE IF EXISTS `papeleria_factura`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `papeleria_factura` (
  `ID_FACTURA` int NOT NULL AUTO_INCREMENT,
  `CANTIDAD_VENDIDA` int NOT NULL,
  `SUBTOTAL_FACTURA` int NOT NULL,
  `TOTAL_FACTURA` int NOT NULL,
  `DESC_FACTURA` decimal(5,2) NOT NULL,
  `FECHA_FACTURA` date NOT NULL,
  `ID_CLIENTE_FACTURA_id` int NOT NULL,
  `ID_PRODUCTO_FACTURA_id` int NOT NULL,
  PRIMARY KEY (`ID_FACTURA`),
  KEY `Papeleria_factura_ID_CLIENTE_FACTURA_i_16044f63_fk_Papeleria` (`ID_CLIENTE_FACTURA_id`),
  KEY `Papeleria_factura_ID_PRODUCTO_FACTURA__db93f0be_fk_Papeleria` (`ID_PRODUCTO_FACTURA_id`),
  CONSTRAINT `Papeleria_factura_ID_CLIENTE_FACTURA_i_16044f63_fk_Papeleria` FOREIGN KEY (`ID_CLIENTE_FACTURA_id`) REFERENCES `papeleria_cliente` (`ID_CLIENTE`),
  CONSTRAINT `Papeleria_factura_ID_PRODUCTO_FACTURA__db93f0be_fk_Papeleria` FOREIGN KEY (`ID_PRODUCTO_FACTURA_id`) REFERENCES `papeleria_producto` (`ID_PRODUCTO`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `papeleria_factura`
--

LOCK TABLES `papeleria_factura` WRITE;
/*!40000 ALTER TABLE `papeleria_factura` DISABLE KEYS */;
INSERT INTO `papeleria_factura` VALUES (1,2,8000,10000,0.00,'2023-11-05',1,2),(2,5,20000,25000,0.00,'2023-11-05',1,2);
/*!40000 ALTER TABLE `papeleria_factura` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `papeleria_movimientoproducto`
--

DROP TABLE IF EXISTS `papeleria_movimientoproducto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `papeleria_movimientoproducto` (
  `ID_MOVIMIENTO` int NOT NULL AUTO_INCREMENT,
  `DESCRIPCION_MOVIMIENTO` varchar(30) NOT NULL,
  `CANTIDAD_MOVIMIENTO` int NOT NULL,
  `FECHA_MOVIMIENTO` date NOT NULL,
  `ID_PRODUCTO_MOVIMIENTO_id` int NOT NULL,
  PRIMARY KEY (`ID_MOVIMIENTO`),
  KEY `Papeleria_movimiento_ID_PRODUCTO_MOVIMIEN_0e1028c5_fk_Papeleria` (`ID_PRODUCTO_MOVIMIENTO_id`),
  CONSTRAINT `Papeleria_movimiento_ID_PRODUCTO_MOVIMIEN_0e1028c5_fk_Papeleria` FOREIGN KEY (`ID_PRODUCTO_MOVIMIENTO_id`) REFERENCES `papeleria_producto` (`ID_PRODUCTO`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `papeleria_movimientoproducto`
--

LOCK TABLES `papeleria_movimientoproducto` WRITE;
/*!40000 ALTER TABLE `papeleria_movimientoproducto` DISABLE KEYS */;
INSERT INTO `papeleria_movimientoproducto` VALUES (12,'Compra a proveedor',10,'2023-11-05',1),(13,'Venta a cliente',5,'2023-11-05',2),(14,'Compra a proveedor',7,'2023-11-05',2),(15,'Compra a proveedor',20,'2023-11-05',3);
/*!40000 ALTER TABLE `papeleria_movimientoproducto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `papeleria_pedido`
--

DROP TABLE IF EXISTS `papeleria_pedido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `papeleria_pedido` (
  `ID_PEDIDO` int NOT NULL AUTO_INCREMENT,
  `CANTIDAD_COMPRADA` int NOT NULL,
  `PRECIO_TOTAL` int NOT NULL,
  `ESTADO_PEDIDO` varchar(1) NOT NULL,
  `ID_PRODUCTO_PEDIDO_id` int NOT NULL,
  `ID_PROVEEDOR_PEDIDO_id` int NOT NULL,
  `FECHA_PEDIDO` date NOT NULL,
  `FECHA_PEDIDO_LLEGADA` date NOT NULL,
  PRIMARY KEY (`ID_PEDIDO`),
  KEY `Papeleria_pedido_ID_PRODUCTO_PEDIDO_i_dc134baa_fk_Papeleria` (`ID_PRODUCTO_PEDIDO_id`),
  KEY `Papeleria_pedido_ID_PROVEEDOR_PEDIDO__7ce469d7_fk_Papeleria` (`ID_PROVEEDOR_PEDIDO_id`),
  CONSTRAINT `Papeleria_pedido_ID_PRODUCTO_PEDIDO_i_dc134baa_fk_Papeleria` FOREIGN KEY (`ID_PRODUCTO_PEDIDO_id`) REFERENCES `papeleria_producto` (`ID_PRODUCTO`),
  CONSTRAINT `Papeleria_pedido_ID_PROVEEDOR_PEDIDO__7ce469d7_fk_Papeleria` FOREIGN KEY (`ID_PROVEEDOR_PEDIDO_id`) REFERENCES `papeleria_proveedor` (`ID_PROVEEDOR`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `papeleria_pedido`
--

LOCK TABLES `papeleria_pedido` WRITE;
/*!40000 ALTER TABLE `papeleria_pedido` DISABLE KEYS */;
INSERT INTO `papeleria_pedido` VALUES (8,10,160000,'A',1,2,'2023-11-05','2023-11-10'),(9,7,21000,'A',2,1,'2023-11-05','2023-11-10');
/*!40000 ALTER TABLE `papeleria_pedido` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `papeleria_producto`
--

DROP TABLE IF EXISTS `papeleria_producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `papeleria_producto` (
  `ID_PRODUCTO` int NOT NULL AUTO_INCREMENT,
  `DESCRIPCION_PRODUCTO` varchar(30) NOT NULL,
  `CANTIDAD_EXIS_PRODUCTO` int NOT NULL,
  `PRECIO_VENTA_PRODUCTO` int NOT NULL,
  `ESTADO_PRODUCTO` varchar(1) NOT NULL,
  `ID_CATEGORIA_PRODUCTO_id` int NOT NULL,
  `IVA_FACTURA` decimal(5,2) NOT NULL,
  PRIMARY KEY (`ID_PRODUCTO`),
  KEY `Papeleria_producto_ID_CATEGORIA_PRODUCT_f591d583_fk_Papeleria` (`ID_CATEGORIA_PRODUCTO_id`),
  CONSTRAINT `Papeleria_producto_ID_CATEGORIA_PRODUCT_f591d583_fk_Papeleria` FOREIGN KEY (`ID_CATEGORIA_PRODUCTO_id`) REFERENCES `papeleria_categoria` (`ID_CATEGORIA`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `papeleria_producto`
--

LOCK TABLES `papeleria_producto` WRITE;
/*!40000 ALTER TABLE `papeleria_producto` DISABLE KEYS */;
INSERT INTO `papeleria_producto` VALUES (1,'Hotwheels',20,10000,'A',1,19.00),(2,'Cuaderno anillado',20,5000,'A',2,15.00),(3,'Papel Carta',70,2000,'A',3,12.00);
/*!40000 ALTER TABLE `papeleria_producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `papeleria_proveedor`
--

DROP TABLE IF EXISTS `papeleria_proveedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `papeleria_proveedor` (
  `ID_PROVEEDOR` int NOT NULL AUTO_INCREMENT,
  `NOMBRE_PROVEEDOR` varchar(30) NOT NULL,
  `DIRECCION_PROVEEDOR` varchar(30) NOT NULL,
  `CORREO_PROVEEDOR` varchar(30) NOT NULL,
  `TELEFONO_PROVEEDOR` varchar(30) NOT NULL,
  `ESTADO_PROVEEDOR` varchar(1) NOT NULL,
  PRIMARY KEY (`ID_PROVEEDOR`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `papeleria_proveedor`
--

LOCK TABLES `papeleria_proveedor` WRITE;
/*!40000 ALTER TABLE `papeleria_proveedor` DISABLE KEYS */;
INSERT INTO `papeleria_proveedor` VALUES (1,'Norma','calle 23','norma@hotmail.com','3503491032','A'),(2,'Mattel','calle 53','mattel@hotmail.com','3049103842','A');
/*!40000 ALTER TABLE `papeleria_proveedor` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-05 21:06:54
