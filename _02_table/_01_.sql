CREATE TABLE `orderextensions` (
  `Id` bigint(20) NOT NULL COMMENT 'id',
  `Order_Id` bigint(20) NOT NULL COMMENT 'oms订单id',
  `ThirdOrderNo` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '第三方订单编码',
  `ParentOrg_Id` bigint(20) NOT NULL COMMENT '服务商id',
  `OrderSouorce` tinyint(4) NOT NULL DEFAULT '0' COMMENT '来源类型，0，易酒批，1、拼多多，2、淘宝，3、京东',
  `CreateTime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `LastUpdateTime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
  PRIMARY KEY (`Id`),
  KEY `Idx_OrderId` (`Order_Id`) USING BTREE,
  KEY `Idx_ThirdOrderNo_ParentOrgId` (`ThirdOrderNo`,`ParentOrg_Id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='第三方订单来源'


CREATE TABLE `yjp_lz_scm_oms_order.orderextensions` (
  Id bigint COMMENT 'id'
  ,Order_Id bigint COMMENT 'oms订单id'
  ,ThirdOrderNo string COMMENT '第三方订单编码'
  ,ParentOrg_Id bigint COMMENT '服务商id'
  ,OrderSouorce tinyint COMMENT '来源类型，0，易酒批，1、拼多多，2、淘宝，3、京东'
  ,CreateTime timestamp COMMENT '创建时间'
  ,LastUpdateTime timestamp COMMENT '修改时间'
  ,_loadtime timestamp
  ,PRIMARY KEY (`Id`,`_database`)
) partition by hash(Id,_database) partitions 3 stored as kudu COMMENT='第三方订单来源'