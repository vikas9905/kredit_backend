--
-- File generated with SQLiteStudio v3.4.3 on Sun Apr 2 16:19:14 2023
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: quiz_answer
CREATE TABLE IF NOT EXISTS "quiz_answer" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "option_id_id" bigint NOT NULL REFERENCES "quiz_options" ("id") DEFERRABLE INITIALLY DEFERRED, "qid_id" bigint NOT NULL REFERENCES "quiz_question" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO quiz_answer (id, option_id_id, qid_id) VALUES (1, 3, 1);
INSERT INTO quiz_answer (id, option_id_id, qid_id) VALUES (2, 6, 2);
INSERT INTO quiz_answer (id, option_id_id, qid_id) VALUES (3, 11, 3);
INSERT INTO quiz_answer (id, option_id_id, qid_id) VALUES (4, 15, 4);
INSERT INTO quiz_answer (id, option_id_id, qid_id) VALUES (5, 17, 5);

-- Table: quiz_options
CREATE TABLE IF NOT EXISTS "quiz_options" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "optionNum" varchar(10) NOT NULL, "optionValue" varchar(200) NOT NULL, "qid_id" bigint NOT NULL REFERENCES "quiz_question" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO quiz_options (id, optionNum, optionValue, qid_id) VALUES (1, 'A', 'mango', 1);
INSERT INTO quiz_options (id, optionNum, optionValue, qid_id) VALUES (2, 'B', 'Apple', 1);
INSERT INTO quiz_options (id, optionNum, optionValue, qid_id) VALUES (3, 'C', 'Soap', 1);
INSERT INTO quiz_options (id, optionNum, optionValue, qid_id) VALUES (4, 'D', 'Grapes', 1);
INSERT INTO quiz_options (id, optionNum, optionValue, qid_id) VALUES (5, 'A', 'heating', 2);
INSERT INTO quiz_options (id, optionNum, optionValue, qid_id) VALUES (6, 'B', 'cooling', 2);
INSERT INTO quiz_options (id, optionNum, optionValue, qid_id) VALUES (7, 'C', 'cooking', 2);
INSERT INTO quiz_options (id, optionNum, optionValue, qid_id) VALUES (8, 'D', 'Don''t Know', 2);
INSERT INTO quiz_options (id, optionNum, optionValue, qid_id) VALUES (9, 'A', 'Fruit', 3);
INSERT INTO quiz_options (id, optionNum, optionValue, qid_id) VALUES (10, 'B', 'oil', 3);
INSERT INTO quiz_options (id, optionNum, optionValue, qid_id) VALUES (11, 'C', 'Milk', 3);
INSERT INTO quiz_options (id, optionNum, optionValue, qid_id) VALUES (12, 'D', 'None', 3);
INSERT INTO quiz_options (id, optionNum, optionValue, qid_id) VALUES (13, 'A', 'heating', 4);
INSERT INTO quiz_options (id, optionNum, optionValue, qid_id) VALUES (14, 'B', 'Cooking', 4);
INSERT INTO quiz_options (id, optionNum, optionValue, qid_id) VALUES (15, 'C', 'Cooling', 4);
INSERT INTO quiz_options (id, optionNum, optionValue, qid_id) VALUES (16, 'D', 'storage', 4);
INSERT INTO quiz_options (id, optionNum, optionValue, qid_id) VALUES (17, 'A', 'Ram', 5);
INSERT INTO quiz_options (id, optionNum, optionValue, qid_id) VALUES (18, 'B', 'Shayam', 5);
INSERT INTO quiz_options (id, optionNum, optionValue, qid_id) VALUES (19, 'C', 'Raja', 5);
INSERT INTO quiz_options (id, optionNum, optionValue, qid_id) VALUES (20, 'D', 'I Killed', 5);
INSERT INTO quiz_options (id, optionNum, optionValue, qid_id) VALUES (21, 'A', 'God', 6);
INSERT INTO quiz_options (id, optionNum, optionValue, qid_id) VALUES (22, 'B', 'Devil', 6);
INSERT INTO quiz_options (id, optionNum, optionValue, qid_id) VALUES (23, 'C', 'Bird', 6);
INSERT INTO quiz_options (id, optionNum, optionValue, qid_id) VALUES (24, 'D', 'None', 6);
INSERT INTO quiz_options (id, optionNum, optionValue, qid_id) VALUES (25, 'A', 'Devi', 7);
INSERT INTO quiz_options (id, optionNum, optionValue, qid_id) VALUES (26, 'B', 'Danav', 7);
INSERT INTO quiz_options (id, optionNum, optionValue, qid_id) VALUES (27, 'C', 'God', 7);
INSERT INTO quiz_options (id, optionNum, optionValue, qid_id) VALUES (28, 'D', 'None', 7);

-- Table: quiz_orderdetails
CREATE TABLE IF NOT EXISTS "quiz_orderdetails" ("order_id" varchar(100) NOT NULL PRIMARY KEY, "ammount_requested" integer NOT NULL, "used_coin" integer NOT NULL, "payment_option_id" bigint NOT NULL REFERENCES "quiz_userpaymentoptions" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id_id" bigint NOT NULL REFERENCES "quiz_user" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Table: quiz_paymentdetails
CREATE TABLE IF NOT EXISTS "quiz_paymentdetails" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "ammount_paid" integer NOT NULL, "payment_status" bool NOT NULL, "for_coins" integer NOT NULL, "comments" varchar(200) NOT NULL, "order_id_id" varchar(100) NOT NULL REFERENCES "quiz_orderdetails" ("order_id") DEFERRABLE INITIALLY DEFERRED);

-- Table: quiz_paymentprovider
CREATE TABLE IF NOT EXISTS "quiz_paymentprovider" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL, "type" varchar(10) NOT NULL);
INSERT INTO quiz_paymentprovider (id, name, type) VALUES (1, 'PhonePe', 'UPI');
INSERT INTO quiz_paymentprovider (id, name, type) VALUES (2, 'PhonePe', 'Wallet');
INSERT INTO quiz_paymentprovider (id, name, type) VALUES (3, 'Paytm', 'UPI');

-- Table: quiz_question
CREATE TABLE IF NOT EXISTS "quiz_question" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "question" varchar(300) NOT NULL, "level" integer NOT NULL, "coins" integer NOT NULL, "tag_id_id" bigint NOT NULL REFERENCES "quiz_questiontag" ("id") DEFERRABLE INITIALLY DEFERRED, "quiz_id_id" bigint NULL REFERENCES "quiz_quizs" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO quiz_question (id, question, level, coins, tag_id_id, quiz_id_id) VALUES (1, 'which item is not eatable?', 0, 1, 1, 1);
INSERT INTO quiz_question (id, question, level, coins, tag_id_id, quiz_id_id) VALUES (2, 'AC is used for?', 0, 1, 1, 1);
INSERT INTO quiz_question (id, question, level, coins, tag_id_id, quiz_id_id) VALUES (3, 'Cow gives us', 0, 1, 1, 1);
INSERT INTO quiz_question (id, question, level, coins, tag_id_id, quiz_id_id) VALUES (4, 'Refrigerator is used for?', 0, 1, 1, 1);
INSERT INTO quiz_question (id, question, level, coins, tag_id_id, quiz_id_id) VALUES (5, 'who killed Ravan?', 0, 1, 1, 1);
INSERT INTO quiz_question (id, question, level, coins, tag_id_id, quiz_id_id) VALUES (6, 'Who is Ravan?', 1, 2, 1, 2);
INSERT INTO quiz_question (id, question, level, coins, tag_id_id, quiz_id_id) VALUES (7, 'Who is Ram?', 1, 2, 1, 2);

-- Table: quiz_questiontag
CREATE TABLE IF NOT EXISTS "quiz_questiontag" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "tag_name" varchar(100) NOT NULL);
INSERT INTO quiz_questiontag (id, tag_name) VALUES (1, 'household');

-- Table: quiz_user
CREATE TABLE IF NOT EXISTS "quiz_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_name" varchar(50) NOT NULL, "user_id" varchar(50) NOT NULL, "total_coins" integer NOT NULL);
INSERT INTO quiz_user (id, user_name, user_id, total_coins) VALUES (2, 'vikas', '1234', 2);

-- Table: quiz_userpaymentoptions
CREATE TABLE IF NOT EXISTS "quiz_userpaymentoptions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(50) NOT NULL, "payment_num" integer NOT NULL, "verified" bool NOT NULL, "provider_id" bigint NOT NULL REFERENCES "quiz_paymentprovider" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id_id" bigint NOT NULL REFERENCES "quiz_user" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Index: quiz_answer_option_id_id_e5798d7a
CREATE INDEX IF NOT EXISTS "quiz_answer_option_id_id_e5798d7a" ON "quiz_answer" ("option_id_id");

-- Index: quiz_answer_qid_id_39aad1eb
CREATE INDEX IF NOT EXISTS "quiz_answer_qid_id_39aad1eb" ON "quiz_answer" ("qid_id");

-- Index: quiz_options_qid_id_516b379e
CREATE INDEX IF NOT EXISTS "quiz_options_qid_id_516b379e" ON "quiz_options" ("qid_id");

-- Index: quiz_orderdetails_payment_option_id_b17dfe29
CREATE INDEX IF NOT EXISTS "quiz_orderdetails_payment_option_id_b17dfe29" ON "quiz_orderdetails" ("payment_option_id");

-- Index: quiz_orderdetails_user_id_id_e6f46d1f
CREATE INDEX IF NOT EXISTS "quiz_orderdetails_user_id_id_e6f46d1f" ON "quiz_orderdetails" ("user_id_id");

-- Index: quiz_paymentdetails_order_id_id_d3aa22b7
CREATE INDEX IF NOT EXISTS "quiz_paymentdetails_order_id_id_d3aa22b7" ON "quiz_paymentdetails" ("order_id_id");

-- Index: quiz_question_tag_id_id_8bd491e4
CREATE INDEX IF NOT EXISTS "quiz_question_tag_id_id_8bd491e4" ON "quiz_question" ("tag_id_id");

-- Index: quiz_userpaymentoptions_provider_id_d2cc02f7
CREATE INDEX IF NOT EXISTS "quiz_userpaymentoptions_provider_id_d2cc02f7" ON "quiz_userpaymentoptions" ("provider_id");

-- Index: quiz_userpaymentoptions_user_id_id_4a3852c1
CREATE INDEX IF NOT EXISTS "quiz_userpaymentoptions_user_id_id_4a3852c1" ON "quiz_userpaymentoptions" ("user_id_id");

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
