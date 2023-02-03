-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 14, 2021 at 10:48 AM
-- Server version: 10.1.29-MariaDB
-- PHP Version: 7.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `py_accounts`
--

-- --------------------------------------------------------

--
-- Table structure for table `accounts`
--

CREATE TABLE `accounts` (
  `id` int(100) NOT NULL,
  `username` varchar(100) NOT NULL,
  `age` int(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `accounts`
--

INSERT INTO `accounts` (`id`, `username`, `age`, `email`, `password`) VALUES
(1, 'Surat Banerjee', 24, 'surat@gmail.com', 'surat'),
(2, 'Moumita Banerjee', 30, 'soumayan.ban@gmail.com', 'moumita'),
(3, 'Soumayan Banerjee', 25, 'soumayan.ban@gmail.com', 'soumayan');

-- --------------------------------------------------------

--
-- Table structure for table `diabetes`
--

CREATE TABLE `diabetes` (
  `id` int(100) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Pregnancics` int(100) NOT NULL,
  `Glucose` int(100) NOT NULL,
  `BloodPressure` int(100) NOT NULL,
  `SkinThick` int(100) NOT NULL,
  `InsulinLev` int(100) NOT NULL,
  `BMI` int(100) NOT NULL,
  `DPF` int(100) NOT NULL,
  `Age` int(100) NOT NULL,
  `Probability` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `diabetes`
--

INSERT INTO `diabetes` (`id`, `Name`, `Pregnancics`, `Glucose`, `BloodPressure`, `SkinThick`, `InsulinLev`, `BMI`, `DPF`, `Age`, `Probability`) VALUES
(1, 'Surat Banerjee', 0, 117, 72, 24, 168, 29, 0, 24, 0);

-- --------------------------------------------------------

--
-- Table structure for table `hdp`
--

CREATE TABLE `hdp` (
  `id` int(100) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Age` int(100) NOT NULL,
  `CP` int(100) NOT NULL,
  `Chol` int(100) NOT NULL,
  `FBP` int(100) NOT NULL,
  `RestECG` int(100) NOT NULL,
  `Thalach` int(100) NOT NULL,
  `EXANG` int(100) NOT NULL,
  `Slope` int(100) NOT NULL,
  `Probability` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `spham`
--

CREATE TABLE `spham` (
  `id` int(100) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Message` varchar(100) NOT NULL,
  `Predict` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `spham`
--

INSERT INTO `spham` (`id`, `Name`, `Message`, `Predict`) VALUES
(1, 'Surat Banerjee', 'Hi Sampurna, nice to meet you.', '[0]');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accounts`
--
ALTER TABLE `accounts`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `diabetes`
--
ALTER TABLE `diabetes`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `hdp`
--
ALTER TABLE `hdp`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `spham`
--
ALTER TABLE `spham`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `accounts`
--
ALTER TABLE `accounts`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `diabetes`
--
ALTER TABLE `diabetes`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `hdp`
--
ALTER TABLE `hdp`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `spham`
--
ALTER TABLE `spham`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
