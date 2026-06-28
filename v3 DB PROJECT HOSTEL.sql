USE hostelmanagement;

CREATE DATABASE hostelManagement;

USE hostelManagement;

CREATE TABLE course (
course_id INT PRIMARY KEY AUTO_INCREMENT,
course_name VARCHAR(50) NOT NULL,
department  VARCHAR(50)  NOT NULL,
duration_years  INT NOT NULL
);

DESCRIBE course;


CREATE TABLE hostel (
    hostel_id INT   PRIMARY KEY AUTO_INCREMENT,
    HostelName VARCHAR(50) NOT NULL,
    location VARCHAR(50) NOT NULL,
    capacity    INT NOT NULL,
    status ENUM('active', 'inactive', 'suspended') DEFAULT 'active' 
);

ALTER TABLE hostel 
MODIFY hostel_id INT;

DESCRIBE hostel;

CREATE TABLE room (
    room_id VARCHAR(10) PRIMARY KEY AUTO_INCREMENT,
    room_number VARCHAR(10) NOT NULL,
    hostel_id VARCHAR(10) NOT NULL,
    capacity INT NOT NULL,
    status ENUM('available', 'occupied', 'maintenance') NOT NULL DEFAULT 'available'
);

DESCRIBE room;


CREATE TABLE warden (
    warden_id VARCHAR(10) PRIMARY KEY AUTO_INCREMENT,
    first_name  VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    contact VARCHAR(14) NOT NULL ,
    hostel_id VARCHAR(10)
);
    
    
CREATE TABLE student (
    student_id VARCHAR(10) PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    contact VARCHAR(20) NOT NULL UNIQUE,
    birth_year YEAR NOT NULL,
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    course_id VARCHAR(10) NOT NULL,
    room_id VARCHAR(10)
);

CREATE TABLE payment (
    payment_id VARCHAR(10) PRIMARY KEY,
    student_id VARCHAR(10) NOT NULL,
    amount INT NOT NULL CHECK (amount > 0),
    payment_date DATE,
    mode_of_payment ENUM('Cash', 'Mobile Money', 'Bank Transfer', 'Card') NOT NULL,
    status ENUM('paid', 'pending', 'overdue') NOT NULL DEFAULT 'pending',
    due_date DATE NOT NULL,
    academic_year VARCHAR(10)     NOT NULL,
    semester ENUM('Semester 1', 'Semester 2') NOT NULL
    
);


INSERT INTO course (course_name, department, duration_years) VALUES
    ('Bachelor of Computer Science',    'School of Computing',       3),
    ('Bachelor of Business Administration', 'School of Business',    3),
    ('Bachelor of Nursing',             'School of Health Sciences', 4),
    ('Bachelor of Civil Engineering',   'School of Engineering',     4),
    ('Bachelor of Education',           'School of Education',       3);


INSERT INTO hostel (HostelName, location, capacity, status) VALUES
('Nile View Hostel',    'Block A, North Campus', 120, 'active'),
('Sunrise Hostel',      'Block B, East Wing',    80,  'active'),
('Victoria Hall',       'Block C, South Campus', 100, 'active'),
('Speke Residence',     'Block D, West Wing',    60,  'inactive'),
('Kampala Heights',     'Block E, Central',      90,  'active');


INSERT INTO visitor (visitor_name, visitor_contact, relationship, gender) VALUES
('Grace Nakato',    '+256700111001', 'Mother',   'Female'),
('James Okello',    '+256700111002', 'Father',   'Male'),
('Mary Achieng',    '+256700111003', 'Sister',   'Female'),
('Robert Tumwine',  '+256700111004', 'Uncle',    'Male'),
('Patricia Nambi',  '+256700111005', 'Guardian', 'Female');


INSERT INTO room (room_number, hostel_id, capacity, status) VALUES
    ('A101', 1, 2, 'occupied'),
    ('A102', 1, 2, 'available'),
    ('A103', 1, 4, 'occupied'),
    ('A104', 1, 2, 'maintenance'),
    ('B201', 2, 2, 'occupied'),
    ('B202', 2, 4, 'available'),
    ('B203', 2, 2, 'occupied'),
    ('C301', 3, 2, 'occupied'),
    ('C302', 3, 4, 'available'),
    ('C303', 3, 2, 'occupied');


INSERT INTO warden (first_name, last_name, contact, hostel_id, gender) VALUES
    ('Samuel',   'Kato',      '+256701000001', 1, 'Male'),
    ('Esther',   'Namukasa',  '+256701000002', 1, 'Female'),
    ('David',    'Ssemakula', '+256701000003', 1, 'Male'),
    ('Florence', 'Atim',      '+256701000004', 2, 'Female'),
    ('Henry',    'Mwesige',   '+256701000005', 2, 'Male'),
    ('Juliet',   'Nabuuma',   '+256701000006', 2, 'Female'),
    ('Paul',     'Oryema',    '+256701000007', 3, 'Male'),
    ('Agnes',    'Akello',    '+256701000008', 3, 'Female'),
    ('Brian',    'Tumusiime', '+256701000009', 3, 'Male'),
    ('Diana',    'Nanteza',   '+256701000010', 4, 'Female');


INSERT INTO student (student_id, first_name, last_name, contact, birth_year, gender, course_id, room_id) VALUES
    (2001, 'Allan',    'Mugisha',   '+256772000001', 2002, 'Male',   1, 1),
    (2002, 'Brenda',   'Nalwoga',   '+256772000002', 2003, 'Female', 2, 2),
    (2003, 'Charles',  'Opio',      '+256772000003', 2001, 'Male',   3, 3),
    (2004, 'Doreen',   'Asiimwe',   '+256772000004', 2002, 'Female', 4, 4),
    (2005, 'Edward',   'Lubega',    '+256772000005', 2003, 'Male',   5, 5),
    (2006, 'Fiona',    'Auma',      '+256772000006', 2002, 'Female', 1, 6),
    (2007, 'George',   'Ssali',     '+256772000007', 2001, 'Male',   2, 7),
    (2008, 'Hannah',   'Nakigozi',  '+256772000008', 2003, 'Female', 3, 8),
    (2009, 'Ivan',     'Okello',    '+256772000009', 2002, 'Male',   4, 9),
    (2010, 'Jane',     'Nambi',     '+256772000010', 2001, 'Female', 5, 10),
    (2011, 'Kevin',    'Byaruhanga','+256772000011', 2003, 'Male',   1, 1),
    (2012, 'Lydia',    'Namatovu',  '+256772000012', 2002, 'Female', 2, 3),
    (2013, 'Martin',   'Agaba',     '+256772000013', 2001, 'Male',   3, 5),
    (2014, 'Norah',    'Achan',     '+256772000014', 2003, 'Female', 4, 7),
    (2015, 'Oscar',    'Tumwine',   '+256772000015', 2002, 'Male',   5, 9),
    (2016, 'Patience', 'Kyomugisha','+256772000016', 2001, 'Female', 1, 2),
    (2017, 'Quinn',    'Wasswa',    '+256772000017', 2003, 'Male',   2, 4),
    (2018, 'Rita',     'Nansubuga', '+256772000018', 2002, 'Female', 3, 6),
    (2019, 'Simon',    'Kafeero',   '+256772000019', 2001, 'Male',   4, 8),
    (2020, 'Tracy',    'Tendo',     '+256772000020', 2003, 'Female', 5, 10);


INSERT INTO payment (payment_id, student_id, amount, payment_date, mode_of_payment, status, due_date, academic_year, semester) VALUES
    (1001, 2001, 850000,  '2024-02-01', 'Mobile Money',  'paid',    '2024-01-31', '2024/2025', 'Semester 1'),
    (1002, 2002, 850000,  '2024-02-03', 'Bank Transfer', 'paid',    '2024-01-31', '2024/2025', 'Semester 1'),
    (1003, 2003, 850000,  NULL,         'Cash',          'pending', '2024-01-31', '2024/2025', 'Semester 1'),
    (1004, 2004, 850000,  '2024-01-28', 'Card',          'paid',    '2024-01-31', '2024/2025', 'Semester 1'),
    (1005, 2005, 850000,  NULL,         'Mobile Money',  'overdue', '2024-01-31', '2024/2025', 'Semester 1'),
    (1006, 2006, 850000,  '2024-02-10', 'Cash',          'paid',    '2024-02-08', '2024/2025', 'Semester 1'),
    (1007, 2007, 850000,  NULL,         'Bank Transfer', 'pending', '2024-02-08', '2024/2025', 'Semester 1'),
    (1008, 2008, 850000,  '2024-02-05', 'Mobile Money',  'paid',    '2024-02-08', '2024/2025', 'Semester 1'),
    (1009, 2009, 850000,  NULL,         'Card',          'overdue', '2024-01-31', '2024/2025', 'Semester 1'),
    (1010, 2010, 850000,  '2024-02-07', 'Cash',          'paid',    '2024-02-08', '2024/2025', 'Semester 1'),
    (1011, 2001, 850000,  '2024-07-01', 'Mobile Money',  'paid',    '2024-06-30', '2024/2025', 'Semester 2'),
    (1012, 2002, 850000,  '2024-07-02', 'Bank Transfer', 'paid',    '2024-06-30', '2024/2025', 'Semester 2'),
    (1013, 2003, 850000,  NULL,         'Mobile Money',  'overdue', '2024-06-30', '2024/2025', 'Semester 2'),
    (1014, 2011, 850000,  '2024-02-02', 'Cash',          'paid',    '2024-01-31', '2024/2025', 'Semester 1'),
    (1015, 2012, 850000,  NULL,         'Card',          'pending', '2024-01-31', '2024/2025', 'Semester 1'),
    (1016, 2013, 900000,  '2024-02-04', 'Mobile Money',  'paid',    '2024-02-08', '2024/2025', 'Semester 1'),
    (1017, 2014, 900000,  NULL,         'Bank Transfer', 'overdue', '2024-01-31', '2024/2025', 'Semester 1'),
    (1018, 2015, 900000,  '2024-02-06', 'Cash',          'paid',    '2024-02-08', '2024/2025', 'Semester 1'),
    (1019, 2016, 850000,  '2024-07-03', 'Mobile Money',  'paid',    '2024-06-30', '2024/2025', 'Semester 2'),
    (1020, 2017, 850000,  NULL,         'Card',          'pending', '2024-06-30', '2024/2025', 'Semester 2');


INSERT INTO visits (student_id, visitor_id, visit_date, visit_time, purpose, status) VALUES
    (2001, 1, '2024-03-01', '10:00:00', 'Family visit',         'completed'),
    (2002, 2, '2024-03-02', '11:30:00', 'Bringing supplies',    'completed'),
    (2003, 3, '2024-03-03', '14:00:00', 'Academic support',     'completed'),
    (2004, 4, '2024-03-04', '09:00:00', 'Family visit',         'completed'),
    (2005, 5, '2024-03-05', '13:00:00', 'Bringing luggage',     'completed'),
    (2006, 1, '2024-03-06', '10:30:00', 'Family visit',         'completed'),
    (2007, 2, '2024-03-07', '15:00:00', 'Bringing food',        'cancelled'),
    (2008, 3, '2024-03-08', '11:00:00', 'Health checkup',       'completed'),
    (2009, 4, '2024-03-09', '14:30:00', 'Family visit',         'scheduled'),
    (2010, 5, '2024-03-10', '09:30:00', 'Bringing supplies',    'scheduled'),
    (2011, 1, '2024-03-11', '10:00:00', 'Family visit',         'completed'),
    (2012, 2, '2024-03-12', '12:00:00', 'Academic discussion',  'completed'),
    (2013, 3, '2024-03-13', '16:00:00', 'Bringing luggage',     'cancelled'),
    (2014, 4, '2024-03-14', '10:00:00', 'Family visit',         'completed'),
    (2015, 5, '2024-03-15', '11:00:00', 'Emergency visit',      'completed'),
    (2001, 2, '2024-04-01', '09:00:00', 'Second family visit',  'completed'),
    (2003, 5, '2024-04-03', '14:00:00', 'Bringing documents',   'scheduled'),
    (2005, 1, '2024-04-05', '13:30:00', 'Family visit',         'completed'),
    (2008, 4, '2024-04-08', '10:00:00', 'Bringing food',        'completed'),
    (2010, 3, '2024-04-10', '15:30:00', 'Family visit',         'scheduled');
    
    describe visits;

SELECT * FROM hostel;
select * from visits;
SELECT * FROM visits where purpose LIKE "Bringing ";
SELECT * FROM visits where purpose LIKE "Family visit ";
select * FROM student;
select * FROM COURSE;
select * FROM ROOM;
select * FROM WARDEN;
select * FROM VISITOR;

  
  
   
SELECT s.student_id, s.first_name, s.last_name,
       r.room_number, h.HostelName
FROM student s
JOIN room r ON s.room_id = r.room_id
JOIN hostel h ON r.hostel_id = h.hostel_id;

SELECT HostelName,
       location,
       capacity
FROM hostel
WHERE hostel_id IN (
    SELECT hostel_id
    FROM room
    WHERE status = 'occupied'
    GROUP BY hostel_id
    HAVING COUNT(room_id) > (
        SELECT capacity / 10
        FROM hostel h2
        WHERE h2.hostel_id = room.hostel_id
    )
);

SELECT student.first_name, student.last_name,
	   course.course_name,payment.status,payment.amount,payment.semester
FROM student
JOIN course ON student.course_id = course.course_id
LEFT JOIN payment ON student.student_id = payment.student_id;

SELECT student.first_name, visitor.visitor_name, visits.visit_date, visits.purpose
FROM student
JOIN visits ON visits.student_id = student.student_id
JOIN visitor on visitor.visitor_id = visits.visitor_id;get_age

DELIMITER $$

CREATE FUNCTION get_balance(p_student_id INT)
RETURNS INT
READS SQL DATA -- Declares that the function reads table data and is not deterministic
BEGIN
    DECLARE total_paid    INT DEFAULT 0;
    DECLARE total_billed  INT DEFAULT 0;
    DECLARE balance       INT DEFAULT 0;
 
    -- Add up everything the student has paid
    SELECT IFNULL(SUM(amount), 0)
    INTO total_paid
    FROM payment
    WHERE student_id = p_student_id
    AND status = 'paid';
 
    -- Count how many payment records exist x 850000 per semester
    SELECT IFNULL(COUNT(*) * 850000, 0)
    INTO total_billed
    FROM payment
    WHERE student_id = p_student_id;
 
    -- Balance IS what they owe minus what they paid
    SET balance = total_billed - total_paid;
 
    RETURN balance; -- Added missing semicolon here
END $$

DELIMITER ;


DELIMITER $$
CREATE FUNCTION get_student_fullname(p_student_id INT)
RETURNS VARCHAR(101)


BEGIN
    DECLARE full_name VARCHAR(101);

    SELECT UPPER(CONCAT(first_name, ' ', last_name))
    INTO full_name
    FROM student
    WHERE student_id = p_student_id;

    RETURN full_name;
END $$
DELIMITER ;

--  Students who have NOT paid
SELECT first_name, last_name
FROM student
WHERE student_id NOT IN (
    SELECT student_id
    FROM payment
    WHERE status = 'paid'
);





CALL get_student();

SELECT * FROM visits;
DESCRIBE course;
DELIMITER $$
CREATE TRIGGER check_payment_status
BEFORE INSERT ON payment
FOR EACH ROW
BEGIN
    IF NEW.payment_date IS NULL AND NEW.due_date < CURDATE() THEN
        SET NEW.status = 'overdue';
    END IF;
END $$
DELIMITER ;



