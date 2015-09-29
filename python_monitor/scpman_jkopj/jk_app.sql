/*
Navicat MySQL Data Transfer

Source Server         : 本地数据库
Source Server Version : 50610
Source Host           : localhost:3306
Source Database       : jk_app

Target Server Type    : MYSQL
Target Server Version : 50610
File Encoding         : 65001

Date: 2013-09-06 11:22:18
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `admin`
-- ----------------------------
DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user` varchar(128) NOT NULL,
  `email` varchar(128) NOT NULL,
  `passwd` varchar(128) NOT NULL,
  `prvili` varchar(3) NOT NULL DEFAULT '0',
  `user_bz` varchar(3) NOT NULL DEFAULT 'Y',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of admin
-- ----------------------------
INSERT INTO `admin` VALUES ('1', 'scpman', 'freeddser@gmail.com', '277d6a2a0177f46eb036ff6c246d5c21', '0', 'Y');

-- ----------------------------
-- Table structure for `jk_host`
-- ----------------------------
DROP TABLE IF EXISTS `jk_host`;
CREATE TABLE `jk_host` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(15) NOT NULL,
  `host_info` varchar(70) NOT NULL,
  `add_time` varchar(30) DEFAULT NULL,
  `en_time` varchar(30) DEFAULT NULL,
  `jk_bz` char(3) NOT NULL DEFAULT 'Y',
  `last_check` varchar(30) DEFAULT NULL,
  `dis_time` varchar(30) DEFAULT NULL,
  `jk_status` varchar(12) NOT NULL COMMENT '0-3正常，错误，未知，停用',
  `jk_color` varchar(12) DEFAULT NULL,
  `jk_type` varchar(12) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=105 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of jk_host
-- ----------------------------
INSERT INTO `jk_host` VALUES ('102', '220.181.111.148', '我的百度', '2013-09-06 11:20:54', '2013-09-06 11:20:54', 'Y', '2013-09-06 11:20:55', null, '正常ping', 'green', 'ping');
INSERT INTO `jk_host` VALUES ('103', '182.254.18.159', 'qq也是我们的了', '2013-09-06 11:21:22', '2013-09-06 11:21:22', 'Y', '2013-09-06 11:21:22', null, '正常ping', 'green', 'ping');
INSERT INTO `jk_host` VALUES ('104', '182.254.18.159', '还是我们的', '2013-09-06 11:21:47', '2013-09-06 11:21:47', 'Y', '2013-09-06 11:21:47', null, '正常-port80', 'green', '80');

-- ----------------------------
-- Table structure for `login_logs`
-- ----------------------------
DROP TABLE IF EXISTS `login_logs`;
CREATE TABLE `login_logs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user` varchar(60) NOT NULL,
  `last_time` varchar(128) NOT NULL,
  `login_ip` varchar(128) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=136 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of login_logs
-- ----------------------------
INSERT INTO `login_logs` VALUES ('128', 'admin', '2013-09-05 11:59:44', '127.0.0.1');
INSERT INTO `login_logs` VALUES ('129', 'admin', '2013-09-05 12:06:35', '127.0.0.1');
INSERT INTO `login_logs` VALUES ('130', 'admin', '2013-09-05 12:18:11', '127.0.0.1');
INSERT INTO `login_logs` VALUES ('131', 'admin', '2013-09-05 12:24:13', '127.0.0.1');
INSERT INTO `login_logs` VALUES ('132', 'admin', '2013-09-05 12:36:06', '127.0.0.1');
INSERT INTO `login_logs` VALUES ('133', 'admin', '2013-09-05 12:45:16', '127.0.0.1');
INSERT INTO `login_logs` VALUES ('134', 'admin', '2013-09-06 09:17:15', '127.0.0.1');
INSERT INTO `login_logs` VALUES ('135', 'scpman', '2013-09-06 11:20:00', '127.0.0.1');

-- ----------------------------
-- Table structure for `view_menu`
-- ----------------------------
DROP TABLE IF EXISTS `view_menu`;
CREATE TABLE `view_menu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `view_menu_name` varchar(200) NOT NULL COMMENT '菜单名',
  `view_menu_zid` int(11) NOT NULL COMMENT '子菜单id',
  `view_menu_bz` char(3) NOT NULL DEFAULT 'Y' COMMENT '是否启用此菜单：Y N',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of view_menu
-- ----------------------------
INSERT INTO `view_menu` VALUES ('1', '监控功能', '1', 'Y');
INSERT INTO `view_menu` VALUES ('2', '批量部署', '2', 'Y');
INSERT INTO `view_menu` VALUES ('3', '性能分析', '3', 'Y');
INSERT INTO `view_menu` VALUES ('4', '其他功能', '4', 'Y');
INSERT INTO `view_menu` VALUES ('5', '计划任务', '5', 'Y');

-- ----------------------------
-- Table structure for `view_zmenu`
-- ----------------------------
DROP TABLE IF EXISTS `view_zmenu`;
CREATE TABLE `view_zmenu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `view_zmenu_name` varchar(200) NOT NULL COMMENT '子菜单名字',
  `xtgnid` int(11) NOT NULL COMMENT 'xt_gongneng_gnid系统功能id',
  `view_menu_zid` int(11) NOT NULL COMMENT '子菜单id',
  `view_menu_zbz` char(3) NOT NULL DEFAULT 'Y' COMMENT '是否启用子菜单Y N',
  PRIMARY KEY (`id`),
  KEY `view_menu_zid` (`view_menu_zid`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of view_zmenu
-- ----------------------------
INSERT INTO `view_zmenu` VALUES ('3', '主机状态监控', '1001', '1', 'Y');
INSERT INTO `view_zmenu` VALUES ('13', '添加新主机', '1002', '1', 'Y');
INSERT INTO `view_zmenu` VALUES ('14', '开发中', '2001', '2', 'Y');
INSERT INTO `view_zmenu` VALUES ('15', '开发中', '3001', '3', 'Y');
INSERT INTO `view_zmenu` VALUES ('16', '开发中', '4001', '4', 'Y');
INSERT INTO `view_zmenu` VALUES ('17', '开发中', '5001', '5', 'Y');

-- ----------------------------
-- Table structure for `xt_gongneng`
-- ----------------------------
DROP TABLE IF EXISTS `xt_gongneng`;
CREATE TABLE `xt_gongneng` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `xtgnid` int(11) NOT NULL COMMENT '系统功能id',
  `xt_gongneng_name` varchar(120) NOT NULL COMMENT '系统功能名字',
  `xt_gongneng_bz` char(3) NOT NULL DEFAULT 'Y' COMMENT '系统功能标志',
  `xt_gongneng_func` varchar(200) NOT NULL COMMENT '系统功能函数',
  `xt_gongneng_url` varchar(200) NOT NULL COMMENT '功能访问url',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of xt_gongneng
-- ----------------------------
INSERT INTO `xt_gongneng` VALUES ('5', '1002', '添加新主机', 'Y', 'app.controllers.chostmonitor.host_add', '/admin/manager/hostmonitor/add/');
INSERT INTO `xt_gongneng` VALUES ('7', '1001', '主机状态监控', 'Y', 'app.controllers.chostmonitor.host_show', '/admin/manager/hostmonitor/');
INSERT INTO `xt_gongneng` VALUES ('8', '1003', '修改主机', 'Y', 'app.controllers.chostmonitor.host_edit', '/admin/manager/hostmonitor/edit/(\\d+)/');
INSERT INTO `xt_gongneng` VALUES ('9', '1004', '停止监控', 'Y', 'app.controllers.chostmonitor.host_disabled', '/admin/manager/hostmonitor/disabled/(\\d+)/');

-- ----------------------------
-- Table structure for `xt_static_var`
-- ----------------------------
DROP TABLE IF EXISTS `xt_static_var`;
CREATE TABLE `xt_static_var` (
  `id` int(11) NOT NULL,
  `des_info` varchar(40) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of xt_static_var
-- ----------------------------
INSERT INTO `xt_static_var` VALUES ('0', '状态正常');
INSERT INTO `xt_static_var` VALUES ('1', '状态错误');
INSERT INTO `xt_static_var` VALUES ('2', '未知错误');
INSERT INTO `xt_static_var` VALUES ('3', '停止监控');
INSERT INTO `xt_static_var` VALUES ('51', 'red');
INSERT INTO `xt_static_var` VALUES ('50', 'green');
INSERT INTO `xt_static_var` VALUES ('52', 'yello');
