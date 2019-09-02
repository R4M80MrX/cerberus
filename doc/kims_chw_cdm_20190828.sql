/*
Navicat MySQL Data Transfer

Source Server         : localhost_mariadb
Source Server Version : 50505
Source Host           : localhost:3306
Source Database       : kims

Target Server Type    : MYSQL
Target Server Version : 50505
File Encoding         : 65001

Date: 2019-08-28 15:32:58
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `cdmalarm`
-- ----------------------------
DROP TABLE IF EXISTS `cdmalarm`;
CREATE TABLE `cdmalarm` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `W_ready` tinyint(1) DEFAULT NULL COMMENT '软件已打开',
  `L_temperature` tinyint(1) DEFAULT NULL COMMENT '激光器温度',
  `L_voltage` tinyint(1) DEFAULT NULL COMMENT '激光器电压',
  `L_fault` tinyint(1) DEFAULT NULL COMMENT '激光器故障',
  `S_state` tinyint(1) DEFAULT NULL COMMENT '振镜状态',
  `ip` int(10) unsigned DEFAULT NULL COMMENT 'use INET_ATON/INET_NTOA',
  `_timestamp` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp() COMMENT '时间戳',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of cdmalarm
-- ----------------------------

-- ----------------------------
-- Table structure for `cdmrecords`
-- ----------------------------
DROP TABLE IF EXISTS `cdmrecords`;
CREATE TABLE `cdmrecords` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `cdmdt` timestamp NULL DEFAULT NULL COMMENT '当前打码日期和时间',
  `cdmcount` int(10) unsigned DEFAULT NULL COMMENT '当前打码数量',
  `cdmcontent` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '当前打码内容',
  `ip` int(10) unsigned DEFAULT NULL COMMENT 'use INET_ATON/INET_NTOA',
  `_timestamp` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp() COMMENT '时间戳',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of cdmrecords
-- ----------------------------

-- ----------------------------
-- Table structure for `chwalarm`
-- ----------------------------
DROP TABLE IF EXISTS `chwalarm`;
CREATE TABLE `chwalarm` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `chwId` int(10) unsigned DEFAULT NULL COMMENT '计量机番号',
  `channelId` int(10) unsigned DEFAULT NULL COMMENT '通道番号',
  `chwAlarmStatus` int(10) unsigned DEFAULT NULL COMMENT '计量机异常状态',
  `faultMode1` int(10) unsigned DEFAULT NULL COMMENT '错误头位模式 No. 13~16',
  `faultMode2` int(10) unsigned DEFAULT NULL COMMENT '错误头位模式 No. 9~12',
  `faultMode3` int(10) unsigned DEFAULT NULL COMMENT '错误头位模式 No. 5~8',
  `faultMode4` int(10) unsigned DEFAULT NULL COMMENT '错误头位模式 No. 1~4',
  `ip` int(10) unsigned DEFAULT NULL COMMENT 'use INET_ATON/INET_NTOA',
  `_timestamp` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp() COMMENT '时间戳',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of chwalarm
-- ----------------------------

-- ----------------------------
-- Table structure for `chwrecords`
-- ----------------------------
DROP TABLE IF EXISTS `chwrecords`;
CREATE TABLE `chwrecords` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `chwId` int(10) unsigned DEFAULT NULL COMMENT '计量机番号',
  `channelId` int(10) unsigned DEFAULT NULL COMMENT '通道番号',
  `bookId` int(10) unsigned DEFAULT NULL COMMENT '预约番号',
  `setpointWeight` float DEFAULT NULL COMMENT '计量设定值',
  `setpointCombination` int(10) unsigned DEFAULT NULL COMMENT '设定个数',
  `statusCombination` int(10) unsigned DEFAULT NULL COMMENT '组合状态(0, 1, 2, 4, 8)',
  `weightCombination` float DEFAULT NULL COMMENT '组合重量',
  `countCombination` int(10) unsigned DEFAULT NULL COMMENT '组合个数',
  `ip` int(10) unsigned DEFAULT NULL COMMENT 'use INET_ATON/INET_NTOA',
  `_timestamp` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp() COMMENT '时间戳',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of chwrecords
-- ----------------------------

-- ----------------------------
-- Table structure for `chwstatus`
-- ----------------------------
DROP TABLE IF EXISTS `chwstatus`;
CREATE TABLE `chwstatus` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `chwId` int(10) unsigned DEFAULT NULL COMMENT '计量机番号',
  `channelId` int(10) unsigned DEFAULT NULL COMMENT '通道番号',
  `chwStatus` int(10) unsigned DEFAULT NULL COMMENT '计量机状态(0~7)',
  `drivePower` int(10) unsigned DEFAULT NULL COMMENT '驱动电源(0=OFF;1=ON)',
  `starved` int(10) unsigned DEFAULT NULL COMMENT '供给不足(0=正常;1=供给不足)',
  `ip` int(10) unsigned DEFAULT NULL COMMENT 'use INET_ATON/INET_NTOA',
  `_timestamp` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp() COMMENT '时间戳',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of chwstatus
-- ----------------------------
