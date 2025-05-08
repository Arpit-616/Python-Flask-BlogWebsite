-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 08, 2025 at 09:06 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `the_ai_coders`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `sl_no` int(50) NOT NULL,
  `name` text NOT NULL,
  `phone_no` int(12) NOT NULL,
  `email` varchar(50) NOT NULL,
  `date` datetime DEFAULT current_timestamp(),
  `msg` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`sl_no`, `name`, `phone_no`, `email`, `date`, `msg`) VALUES
(15, 'reed', 741852963, 'reed@gamil.com', '2025-04-18 12:44:42', 'Hii !! reed ,I am doom, victor von doom.');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sl_no` int(11) NOT NULL,
  `title` varchar(200) NOT NULL,
  `tagline` text NOT NULL,
  `slug` varchar(120) NOT NULL,
  `content` varchar(2000) NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sl_no`, `title`, `tagline`, `slug`, `content`, `date`) VALUES
(1, 'fantastic four:First Step', 'good morning', 'first-post', 'ok', '2025-05-03 00:00:00'),
(2, 'Elon Musk’s Grok AI Now Gets ‘Vision Abilities’ And Real-Time Voice Mode: What Is It And How It Works', 'Grok AI Vision: How It Works ', 'second-post', 'The first thing you should know is that Grok Vision works on iOS and Android devices using the Grok app which sees itself as an AI assistant. xAI says the new Vision and real-time search is available for all users, including those on the SuperGrok plan using their Android phones. Introducing Grok Vision, multilingual audio, and realtime search in Voice Mode.', '2025-05-07 14:09:48'),
(3, 'A faster way to solve complex planning problems', 'Damn', 'third-post', 'By eliminating redundant computations, a new data-driven method can streamline processes like scheduling trains, routing delivery drivers, or assigning airline crews.', '2025-04-19 02:22:31'),
(4, 'Training LLMs to self-detoxify their language', 'Really!!', 'fourth-post', 'A new method from the MIT-IBM Watson AI Lab helps large language models to steer their own responses toward safer, more ethical, value-aligned outputs.', '2025-04-19 02:23:32'),
(5, 'New method assesses and improves the reliability of radiologists’ diagnostic reports', 'what??', 'fifth-post', 'The framework helps clinicians choose phrases that more accurately reflect the likelihood that certain conditions are present in X-rays.', '2025-04-19 02:24:35'),
(6, 'Could LLMs help design our next medicines and materials?', 'wow ok', 'sixth-post', 'A new method lets users ask, in plain language, for a new molecule with certain properties, and receive a detailed description of how to synthesize it.', '2025-05-03 00:00:00'),
(7, 'Google Gemini 2.5 Pro Preview launched', 'Build rich, interactive web apps with an updated Gemini 2.5 Pro', 'seventh-post', 'Google is all set to host its annual developer conference Google I/O 2025 this month. However, ahead of its annual software event, the tech giant has launched a new version of its AI model Gemini. The company has now unenvied Gemini 2.5 Pro Preview which is an updated version of its flagship Gemini 2.5 Pro AI model. The company unveiled the new model, named Gemini 2.5 Pro Preview (I/O edition), earlier than initially planned, aiming to provide developers with early access to its enhanced features. As per Google, the Gemini 2.5 Pro Preview comes with improvements across coding domains.', '2025-05-07 14:04:16');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`sl_no`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sl_no`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `sl_no` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sl_no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
