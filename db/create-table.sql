create schema dbhackingher;

CREATE TABLE image (
    id INT AUTO_INCREMENT PRIMARY KEY,
    content LONGBLOB NOT NULL,
    description VARCHAR(255),
    credit VARCHAR(50)
);

CREATE TABLE quizType (
    id INT AUTO_INCREMENT PRIMARY KEY,
    description VARCHAR(100) NOT NULL
);

CREATE TABLE quiz (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description VARCHAR(255) NOT NULL,
    id_quiz_type INT NOT NULL,
    FOREIGN KEY (id_quiz_type) REFERENCES quizType(id)
);

CREATE TABLE question (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description VARCHAR(255) NOT NULL,
    id_image INT,
    id_quiz INT NOT NULL,
    FOREIGN KEY (id_image) REFERENCES image(id),
    FOREIGN KEY (id_quiz) REFERENCES quiz(id)
);

CREATE TABLE question_option (
    id INT AUTO_INCREMENT PRIMARY KEY,
    description VARCHAR(100),
    points INT NOT NULL,
    id_image INT,
    id_question INT NOT NULL,
    FOREIGN KEY (id_image) REFERENCES image(id),
    FOREIGN KEY (id_question) REFERENCES question(id)
);

CREATE TABLE career_option (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    id_image INT,
    FOREIGN KEY (id_image) REFERENCES image(id)
);

CREATE TABLE result (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_quiz INT NOT NULL,
    min_points INT NOT NULL,
    max_points INT NOT NULL,
    id_career_option INT NOT NULL,
    FOREIGN KEY (id_quiz) REFERENCES quiz(id),
    FOREIGN KEY (id_career_option) REFERENCES career_option(id)
);

CREATE TABLE course (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description VARCHAR(255) NOT NULL,
    link VARCHAR(255) NOT NULL,
    image LONGBLOB,
    id_career_option INT NOT NULL,
    FOREIGN KEY (id_career_option) REFERENCES career_option(id)
);