drop database if exists tianli1;

create database tianli1  DEFAULT CHARACTER SET utf8;

use tianli1;

CREATE TABLE IF NOT EXISTS `sys_industry` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL DEFAULT '',
  `deleted` tinyint(1) DEFAULT 0,
  `status` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

CREATE TABLE IF NOT EXISTS `sys_country` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL DEFAULT '',
  `deleted` tinyint(1) DEFAULT 0,
  `status` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;


CREATE TABLE IF NOT EXISTS `sys_province` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL DEFAULT '',
  `country_id` bigint(20)  NOT NULL,
  `deleted` tinyint(1) DEFAULT 0,
  `status` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;


CREATE TABLE IF NOT EXISTS `sys_city` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL DEFAULT '',
  `province_id` bigint(20) NOT NULL,
  `country_id` bigint(20) NOT NULL,
  `deleted` tinyint(1) DEFAULT 0,
  `status` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;



              
CREATE TABLE IF NOT EXISTS `admin` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL DEFAULT '',
  `password` varchar(100) NOT NULL,
  `role_id` bigint(20) NOT NULL,
  `deleted` tinyint(1) DEFAULT 0,
  `status` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;



CREATE TABLE IF NOT EXISTS `role` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `operation` text NOT NULL,
  `type` int(10) DEFAULT NULL,
  `deleted` tinyint(1) DEFAULT 0,
  `status` tinyint(1) NOT NULL DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

CREATE TABLE IF NOT EXISTS `email_apply` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `email` varchar(255) NOT NULL,
  `code` varchar(100) NOT NULL,
  `date_created` datetime NOT NULL,
  `deleted` tinyint(1) DEFAULT 0,
  `status` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

CREATE TABLE IF NOT EXISTS `white_email_list` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email_suffix` varchar(100) NOT NULL,
  `description` varchar(255) ,
  `deleted` tinyint(1) DEFAULT 0,
  `status` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;


CREATE TABLE IF NOT EXISTS `user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `email` varchar(30) NOT NULL DEFAULT '',
  `password` varchar(100) NOT NULL,
  `screenname` varchar(30) NOT NULL,
  `sex` tinyint(1) NOT NULL,
  `birth_date` datetime ,
  `date_created` datetime NOT NULL,
  `avatar` varchar(255) NOT NULL,
  `point` bigint(20) NOT NULL,
  `deleted` tinyint(1) DEFAULT 0,
  `status` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;


CREATE TABLE IF NOT EXISTS `user_content_hidden` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) NOT NULL,
  `type` tinyint(1) NOT NULL,
  `object_id` bigint(20) NOT NULL,
  `deleted` tinyint(1) DEFAULT 0,
  `status` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;



CREATE TABLE IF NOT EXISTS `gcm_information` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) NOT NULL,
  `device_token` varchar(255) NOT NULL,
  `create_date` datetime NOT NULL,
  `update_date` datetime NOT NULL,
  `deleted` tinyint(1) DEFAULT 0,
  `status` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;



CREATE TABLE IF NOT EXISTS `user_private_file` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) NOT NULL, 
  `file_name` varchar(100) NOT NULL,
  `ext` varchar(100),
  `file` varchar(255) NOT NULL,
  `size` bigint(20) NOT NULL,
  `create_date` datetime NOT NULL,
  `deleted` tinyint(1) DEFAULT 0,
  `status` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

CREATE TABLE IF NOT EXISTS `company` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL DEFAULT '',
   `user_id` bigint(20),
  `user_screenname` varchar(255), 
  `province` varchar(255)  ,
  `city` varchar(255)  ,
  `district` varchar(255) ,
   `street` varchar(255) ,
  `address` varchar(255) ,
  `industry_id` bigint(20) NOT NULL,
  `contact` varchar(30),
  `email` varchar(100) NOT NULL,
  `email_suffix` varchar(100) NOT NULL,
  `phone` varchar(30) NOT NULL,
  `description` text ,
  `entry_date` datetime,
  `date_created` datetime NOT NULL,
  `logo` varchar(255) NOT NULL,
  `deleted` tinyint(1) DEFAULT 0,
  `status` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;


CREATE TABLE IF NOT EXISTS `company_user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20)  NOT NULL, 
  `company_id` bigint(20) NOT NULL,
  `company_name` varchar(50) NOT NULL,
  `role` tinyint(1) DEFAULT 2,
  `title` varchar(50),
  `phone` varchar(30),
  `office_phone` varchar(30),
  `entry_date` datetime,
  `deleted` tinyint(1) DEFAULT 0,
  `status` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;



CREATE TABLE IF NOT EXISTS `company_department` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `company_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `user_screenname` varchar(255), 
  `name` varchar(255) NOT NULL, 
  `type` tinyint(1) DEFAULT 1 ,
  `project_id` bigint(20) NOT NULL,
  `member_number` int(10) NOT NULL DEFAULT 0,
  `create_date` datetime NOT NULL,
  `deleted` tinyint(1) DEFAULT 0,
  `status` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;


CREATE TABLE IF NOT EXISTS `company_department_user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) NOT NULL, 
  `user_company_id` bigint(20) NOT NULL, 
  `email` varchar(255),
  `company_department_id` bigint(20) NOT NULL,
  `role` tinyint(1) DEFAULT 2,
  `date_created` datetime NOT NULL,
  `deleted` tinyint(1) DEFAULT 0,
  `status` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;


CREATE TABLE IF NOT EXISTS `event` (
  `id` bigint(20)  NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) NOT NULL, 
  `title` varchar(30) NOT NULL, 
  `description` text ,
    `province` varchar(255)  ,
  `city` varchar(255)  ,
  `district` varchar(255) ,
  `street` varchar(255) ,
  `address` varchar(255) ,
  `create_date` datetime NOT NULL,
  `if_all_day` tinyint(1) DEFAULT 0,
  `start_date` datetime NOT NULL,
  `end_date` datetime NOT NULL,
  `if_remind` tinyint(1) DEFAULT 0,
  `if_repeat` tinyint(1) DEFAULT 0,
  `project_id` bigint(20) DEFAULT 0, 
  `type` tinyint(1) DEFAULT 1 COMMENT '1. user-create; 2. task-deadline',
  `deleted` tinyint(1) DEFAULT 0,
  `status` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1 ;




CREATE TABLE IF NOT EXISTS `event_user` (
  `id` bigint(20)  NOT NULL AUTO_INCREMENT,
  `event_id` bigint(20) NOT NULL, 
  `user_id` bigint(20) NOT NULL, 
  `user_company_id` bigint(20) NOT NULL, 
  `user_screenname` varchar(255),
  `email` varchar(255),
  `deleted` tinyint(1) DEFAULT 0,
  `status` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1 ;

CREATE TABLE IF NOT EXISTS `event_repeat` (
  `id` bigint(20)  NOT NULL AUTO_INCREMENT,
  `event_id` bigint(20) NOT NULL, 
  `type` tinyint(1) DEFAULT 1 ,
  `repeat_number` int(10) NOT NULL, 
	`end_type` tinyint(1) not null DEFAULT 3,
	`end_number` int(10) DEFAULT NULL,
	`end_date` datetime DEFAULT NULL,
  `deleted` tinyint(1) DEFAULT 0,
  `status` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1 ;


CREATE TABLE IF NOT EXISTS `event_repeat_date` (
  `id` bigint(20)  NOT NULL AUTO_INCREMENT,
  `event_id` bigint(20) NOT NULL, 
`event_repeat_id` bigint(20) NOT NULL, 
 `remind_start_date` datetime ,
  `remind_end_date` datetime ,
 `start_date` datetime NOT NULL,
  `end_date` datetime NOT NULL,
  `remind_status` tinyint(1) DEFAULT 0,
  `deleted` tinyint(1) DEFAULT 0,
  `status` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1 ;


CREATE TABLE IF NOT EXISTS `event_object_remind` (
  `id` bigint(20)  NOT NULL AUTO_INCREMENT,
  `type` tinyint(1) DEFAULT 0,
  `option_id` bigint(20) NOT NULL, 
  `start_end_type` tinyint(1) DEFAULT 1,
  `deleted` tinyint(1) DEFAULT 0,
  `status` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1 ;


CREATE TABLE IF NOT EXISTS `event_remind` (
  `id` bigint(20)  NOT NULL AUTO_INCREMENT,
  `event_id` bigint(20) NOT NULL, 
  `type` tinyint(1) DEFAULT 1 ,
  `deleted` tinyint(1) DEFAULT 0,
  `status` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1 ;


CREATE TABLE IF NOT EXISTS `contact` (
  `id` bigint(20)  NOT NULL AUTO_INCREMENT,
  `from_user_id` bigint(20) NOT NULL, 
  `to_user_id` bigint(20) NOT NULL, 
  `create_date` datetime NOT NULL ,
  `update_date` datetime NOT NULL,
  `type` int(10) DEFAULT 1 ,
  `deleted` tinyint(1) DEFAULT 0,
  `status` tinyint(1) DEFAULT 10 ,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1 ;

CREATE TABLE IF NOT EXISTS `attention` (
  `id` bigint(20)  NOT NULL AUTO_INCREMENT,
  `from_user_id` bigint(20) NOT NULL, 
  `to_user_id` bigint(20) NOT NULL, 
  `create_date` datetime NOT NULL ,
  `deleted` tinyint(1) DEFAULT 0,
  `status` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1 ;

CREATE TABLE IF NOT EXISTS `feed` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) NOT NULL, 
  `company_id` bigint(20) NOT NULL, 
  `post` varchar(140) NOT NULL DEFAULT '',
  `type` tinyint(1) NOT NULL DEFAULT 1 ,
  `create_date` datetime NOT NULL,
  `origin` tinyint(1) NOT NULL DEFAULT 1 ,
  `origin_id` bigint(20) DEFAULT 0,
  `origin_message` varchar(255),
   `origin_status`  tinyint(1) DEFAULT 0,
  `if_public` tinyint(1) DEFAULT 0,
  `comment_number` int(10) NOT NULL DEFAULT 0,
  `forward_number` int(10) NOT NULL DEFAULT 0, 
  `like_number` int(10) NOT NULL DEFAULT 0,
  `deleted` tinyint(1) DEFAULT 0,
  `status` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

CREATE TABLE IF NOT EXISTS `feed_remind_user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `feed_id` bigint(20) NOT NULL, 
  `user_id` bigint(20) NOT NULL, 
  `user_screenname` varchar(255) NOT NULL, 
  `deleted` tinyint(1) DEFAULT 0,
  `status` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;


CREATE TABLE IF NOT EXISTS `feed_forward` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `from_feed_id` bigint(20) NOT NULL,
  `from_user_id` bigint(20) NOT NULL,
  `from_user_screenname` varchar(30) NOT NULL, 
  `from_user_avatar` varchar(255) NOT NULL, 
  `to_feed_id` bigint(20) NOT NULL, 
  `to_user_id` bigint(20) NOT NULL,
  `to_user_screenname` varchar(30) NOT NULL, 
  `to_user_avatar` varchar(255) NOT NULL, 
  `forward_comment` varchar(255), 
  `create_date` datetime NOT NULL,
  `deleted` tinyint(1) DEFAULT 0,
  `status` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;



CREATE TABLE IF NOT EXISTS `feed_company_department` (
 `id` bigint(20)  NOT NULL AUTO_INCREMENT,
 `feed_id` bigint(20) NOT NULL, 
 `if_share_to_company` tinyint(1) NOT NULL DEFAULT 0,
 `company_id` bigint(20) NOT NULL, 
 `company_department_id` bigint(20) NOT NULL, 
 `deleted` tinyint(1) DEFAULT 0,
 `status` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8  AUTO_INCREMENT=1 ;



CREATE TABLE IF NOT EXISTS `feed_attachment` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `feed_id` bigint(20) NOT NULL, 
   `file_name` varchar(100) NOT NULL,
  `ext` varchar(100),
  `file` varchar(255) NOT NULL,
  `size` bigint(20) NOT NULL,
  `deleted` tinyint(1) DEFAULT 0,
  `status` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;



CREATE TABLE IF NOT EXISTS `feed_comment` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `feed_id` bigint(20) NOT NULL,
  `parent_id` bigint(20) NOT NULL DEFAULT 0,
  `from_user_id` bigint(20) NOT NULL, 
  `from_user_screenname` varchar(30) NOT NULL,
  `from_user_avatar` varchar(100) NOT NULL,
  `to_user_id` bigint(20) NOT NULL, 
  `to_user_screenname` varchar(30) NOT NULL,
  `to_user_avatar` varchar(100) NOT NULL,
  `comment` text,
  `create_date` datetime NOT NULL,
  `deleted` tinyint(1) DEFAULT 0,
  `status` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;


CREATE TABLE IF NOT EXISTS `feed_like` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `feed_id` bigint(20) NOT NULL,
  `user_id` bigint(20)  NOT NULL, 
  `create_date` datetime NOT NULL,
  `unlike` tinyint(1) DEFAULT 0,
  `deleted` tinyint(1) DEFAULT 0,
  `status` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;


CREATE TABLE IF NOT EXISTS `feed_fav` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `feed_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL, 
  `create_date` datetime NOT NULL,
  `unfav` tinyint(1) DEFAULT 0,
  `deleted` tinyint(1) DEFAULT 0,
  `status` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;


CREATE TABLE IF NOT EXISTS `feed_tag` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `feed_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `tag` varchar(140) NOT NULL DEFAULT '',
  `create_date` datetime NOT NULL,
  `deleted` tinyint(1) DEFAULT 0,
  `status` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;




CREATE TABLE IF NOT EXISTS `tag` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `tag` varchar(140) NOT NULL DEFAULT '',
  `create_date` datetime NOT NULL,
  `count` int(10) NOT NULL DEFAULT 0,
  `deleted` tinyint(1) DEFAULT 0,
  `status` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;




CREATE TABLE IF NOT EXISTS `message` (
  `id`bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id`bigint(20) NOT NULL, 
  `title` varchar(255),
  `content` text  ,
  `type` tinyint(1) DEFAULT 1,
  `message_group_id` bigint(20) NOT NULL DEFAULT 0, 
  `create_date` datetime NOT NULL,
  `deleted` tinyint(1) DEFAULT 0,
  `status` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;


CREATE TABLE IF NOT EXISTS `message_direction` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `message_id` bigint(20) NOT NULL, 
  `to_user_id` bigint(20) NOT NULL, 
  `deleted` tinyint(1) DEFAULT 0,
  `status` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;



CREATE TABLE IF NOT EXISTS `message_group` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `company_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL, 
  `title` varchar(140) NOT NULL DEFAULT '',
  `create_date` datetime NOT NULL,
  `deleted` tinyint(1) DEFAULT 0,
  `status` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;


CREATE TABLE IF NOT EXISTS `message_group_user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) NOT NULL, 
	`user_company_id` bigint(20) NOT NULL, 
  `message_group_id` bigint(20) NOT NULL, 
  `date_created` datetime NOT NULL,
  `role` tinyint(1) DEFAULT 2,
  `deleted` tinyint(1) DEFAULT 0,
  `status` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;





CREATE TABLE IF NOT EXISTS `project` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) NOT NULL, 
  `company_id` bigint(20) NOT NULL, 
  `type` tinyint(1) NOT NULL DEFAULT 2,
  `name` varchar(140) NOT NULL,
  `short_name` varchar(255) ,
  `contact_way` varchar(255) ,
  `email` varchar(255),
  `fax` varchar(255) ,
  `start_date` datetime,
  `end_date` datetime,
  `create_date` datetime NOT NULL,
    `province` varchar(255)  ,
  `city` varchar(255)  ,
  `district` varchar(255) ,
   `street` varchar(255) ,
  `address` varchar(255) ,
  `description` text,
  `deleted` tinyint(1) DEFAULT 0,
  `status` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

CREATE TABLE IF NOT EXISTS `project_file` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `project_id` bigint(20) NOT NULL, 
  `user_id` bigint(20) NOT NULL,
  `user_screenname` varchar(30) NOT NULL,
  `file_name` varchar(100) NOT NULL,
  `ext` varchar(100),
  `file` varchar(255) NOT NULL,
  `size` bigint(20) NOT NULL,
  `create_date` datetime NOT NULL,
  `deleted` tinyint(1) DEFAULT 0,
  `status` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;


CREATE TABLE IF NOT EXISTS `project_user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `project_id` bigint(20) NOT NULL, 
  `user_id` bigint(20) NOT NULL,
  `user_company_id` bigint(20) NOT NULL, 
  `user_screenname` varchar(255),
  `email` varchar(255),
  `type` int(10) DEFAULT 0 ,
  `deleted` tinyint(1) DEFAULT 0,
  `status` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;


CREATE TABLE IF NOT EXISTS `task` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) NOT NULL, 
  `project_id` bigint(20) NOT NULL, 
  `company_id` bigint(20) NOT NULL, 
  `title` varchar(140) NOT NULL DEFAULT '',
  `content` text  ,
  `type` tinyint(1) NOT NULL DEFAULT 1 ,
  `create_date` datetime NOT NULL,
  `deadline_date` datetime ,
  `finish_date` datetime,
  `if_private` tinyint(1) DEFAULT 1,
  `if_lock` tinyint(1) DEFAULT 0,
  `color` tinyint(1) NOT NULL,
  `deleted` tinyint(1) DEFAULT 0,
  `status` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;


CREATE TABLE IF NOT EXISTS `task_relation` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `parent_id` bigint(20) NOT NULL, 
  `child_id` bigint(20) NOT NULL, 
  `create_date` datetime NOT NULL,
  `deleted` tinyint(1) DEFAULT 0,
  `status` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

CREATE TABLE IF NOT EXISTS `task_comment` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `task_id` bigint(20) NOT NULL, 
  `user_id` bigint(20) NOT NULL, 
  `content` text , 
  `create_date` datetime NOT NULL,
  `type` tinyint(1) NOT NULL DEFAULT 1,
  `deleted` tinyint(1) DEFAULT 0,
  `status` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

CREATE TABLE IF NOT EXISTS `task_file` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `type`  tinyint(1) NOT NULL,
  `option_id`bigint(20) NOT NULL, 
  `task_id` bigint(20) NOT NULL, 
  `file_name` varchar(100) NOT NULL,
  `ext` varchar(100),
  `file` varchar(255) NOT NULL,
  `size` bigint(20) NOT NULL,
  `deleted` tinyint(1) DEFAULT 0,
  `status` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;


CREATE TABLE IF NOT EXISTS `task_user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `task_id` bigint(20) NOT NULL, 
  `user_id` bigint(20) NOT NULL,
  `user_company_id` bigint(20) NOT NULL, 
  `user_screenname` varchar(255),
  `email` varchar(255),
  `type` int(10) DEFAULT 0 ,
  `if_hidden` tinyint(1) DEFAULT 0,
  `deleted` tinyint(1) DEFAULT 0,
  `status` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;



CREATE TABLE IF NOT EXISTS `task_vote` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `task_id` bigint(20) NOT NULL, 
  `content` varchar(100) NOT NULL DEFAULT '',
  `deleted` tinyint(1) DEFAULT 0,
  `status` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;


CREATE TABLE IF NOT EXISTS `task_vote_result` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `task_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `task_vote_id` bigint (100) NOT NULL,
  `deleted` tinyint(1) DEFAULT 0,
  `status` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

CREATE TABLE IF NOT EXISTS `task_todo` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `task_id` bigint(20) NOT NULL, 
  `task_user_id` bigint(20) NOT NULL, 
  `todo_item` varchar(100) NOT NULL DEFAULT '',
  `sort_order` int(10) NOT NULL DEFAULT 0,
  `create_date` datetime NOT NULL,
  `deadline_date` datetime NOT NULL,
  `finish_date` datetime,
  `deleted` tinyint(1) DEFAULT 0,
  `status` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;


CREATE TABLE IF NOT EXISTS  `user_notify`(
	`id` bigint(20) NOT NULL AUTO_INCREMENT,
	`user_id` bigint(20) NOT NULL,
    `main_button` tinyint(1) DEFAULT 1,
     `pointme_button` tinyint(1) DEFAULT 1,
     `discuss_button` tinyint(1) DEFAULT 1,
   `good_button` tinyint(1) DEFAULT 1,
   `news_button` tinyint(1) DEFAULT 1,
   `deleted` tinyint(1) DEFAULT 0,
	PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;

CREATE TABLE IF NOT EXISTS  `user_hide`(
	`id` bigint(20) NOT NULL AUTO_INCREMENT,
	`user_id` bigint(20) NOT NULL,
   `deleted` tinyint(1) DEFAULT 0,
   `status` tinyint(1) DEFAULT 1,
	PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;

CREATE TABLE IF NOT EXISTS `feed_back` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `u_id` bigint(20) NOT NULL,
  `content` text NOT NULL DEFAULT '',
  `deleted` tinyint(1) DEFAULT 0,
  `status` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;


CREATE TABLE IF NOT EXISTS `notification` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `to_user_id` bigint(20) NOT NULL, 
  `to_email` varchar(255), 
  `from_user_id` bigint(20) NOT NULL, 
  `company_id` bigint(20) NOT NULL, 
  `kind` tinyint(1) NOT NULL,
  `type` int(10) NOT NULL,
  `message` varchar(255),  
  `option_id1` bigint(20) NOT NULL, 
  `option_id2` bigint(20) NOT NULL, 
  `send_status` tinyint(1) NOT NULL,
  `read_status` tinyint(1) NOT NULL,
  `create_date` datetime NOT NULL,
  `status` tinyint(1) DEFAULT 1,
  `deleted` tinyint(1) DEFAULT 0,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;


CREATE TABLE IF NOT EXISTS `stop_user_notification` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `from_user_id` bigint(20) NOT NULL,
  `to_user_id` bigint(20) NOT NULL,
  `type` tinyint(1) NOT NULL,
  `create_date` datetime NOT NULL,
  `status` tinyint(1) DEFAULT 1,
  `deleted` tinyint(1) DEFAULT 0,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;




