CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    description VARCHAR(255) NOT NULL
);

INSERT INTO items (description) VALUES ('Item 1');
INSERT INTO items (description) VALUES ('Item 2');
INSERT INTO items (description) VALUES ('Item 3');
