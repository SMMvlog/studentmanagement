-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 22, 2020 at 10:42 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `student_management`
--

-- --------------------------------------------------------

--
-- Table structure for table `management`
--

CREATE TABLE `management` (
  `RollNo` int(11) NOT NULL,
  `Name` varchar(20) NOT NULL,
  `Email` int(20) NOT NULL,
  `Gender` varchar(20) NOT NULL,
  `Contact` int(20) NOT NULL,
  `DOB` varchar(20) NOT NULL,
  `Address` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `management`
--

INSERT INTO `management` (`RollNo`, `Name`, `Email`, `Gender`, `Contact`, `DOB`, `Address`) VALUES
(1, 'Mehboob', 0, 'Male', 2147483647, '09-10-95', 'Thane India\n\n'),
(2, 'er', 0, 'Male', 9876, 'dssf', 'szdsada\n\n'),
(3, 'sdfsdf', 0, 'Male', 9876, 'dssf', 'szdsada\n'),
(4, 'sdfsdf', 0, 'Male', 9876, 'dssf', 'szdsada\n');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
