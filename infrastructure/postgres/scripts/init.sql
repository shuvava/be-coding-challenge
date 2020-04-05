CREATE SCHEMA dbo;
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE TABLE IF NOT EXISTS dbo.persons (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    firstName varchar(150) not null,
    lastName varchar(150) not null,
    phone varchar(15),
    email varchar(100),
    birthDate timestamp default '-infinity' not null
);
CREATE TABLE IF NOT EXISTS dbo.relation_types (
    id integer not null constraint "relation_types_pk" primary key,
    name varchar(100)
);
CREATE TABLE IF NOT EXISTS dbo.relations
(
	parent_id uuid
		constraint relations_persons_id_fk
			references dbo.persons
				on delete cascade,
	relation_type int
		constraint relations_relation_types_id_fk
			references dbo.relation_types
				on update cascade on delete cascade,
	child_id uuid
		constraint relations_persons_id_fk_2
			references dbo.persons
				on delete cascade
);

alter role family set search_path = "dbo", public;
INSERT INTO dbo.relation_types ("id", "name")
VALUES (1, 'parent'),
(2, 'child')
ON CONFLICT ("id") DO NOTHING;
INSERT INTO dbo.persons (id, firstName, lastName, phone, email, birthDate)
VALUES ('81d2b0ff-0060-42d6-8285-a1f25e7c4036','Ivan', 'Ivanov', '123456789', 'ivan@gmail.com','1981-01-01'),
       ('671135d3-4b5b-4ec1-85a5-a15ef9372f7e','Petr', 'Ivanov', null, 'petr@gmail.com','1980-01-01'),
       ('942723e7-20de-4a62-bd97-e6ffe7c4a209','Gregory', 'Ivanov', null, 'petr@gmail.com','1920-01-01'),
       ('aedf7aee-b28c-49b6-848c-7f58bfe32a5b','John', 'Doe', null, null,'1977-01-01'),
       ('d8c344d1-ddad-420f-ba71-d771d0b4b728','Emily', 'Doe', null, null,'1977-10-01'),
       ('892f8371-20d5-4e97-8a39-ed24b3b9be98','Alex', 'Tretyakov', null, null,'1977-10-01')
ON CONFLICT ("id") DO NOTHING;
INSERT INTO dbo.relations (parent_id, relation_type, child_id)
VALUES ('942723e7-20de-4a62-bd97-e6ffe7c4a209', 1, '81d2b0ff-0060-42d6-8285-a1f25e7c4036'),
       ('942723e7-20de-4a62-bd97-e6ffe7c4a209', 1, '671135d3-4b5b-4ec1-85a5-a15ef9372f7e'),
       ('81d2b0ff-0060-42d6-8285-a1f25e7c4036', 2, '942723e7-20de-4a62-bd97-e6ffe7c4a209'),
       ('671135d3-4b5b-4ec1-85a5-a15ef9372f7e', 2, '942723e7-20de-4a62-bd97-e6ffe7c4a209'),
       ('81d2b0ff-0060-42d6-8285-a1f25e7c4036',1,'aedf7aee-b28c-49b6-848c-7f58bfe32a5b'),
       ('81d2b0ff-0060-42d6-8285-a1f25e7c4036',1,'d8c344d1-ddad-420f-ba71-d771d0b4b728'),
       ('aedf7aee-b28c-49b6-848c-7f58bfe32a5b',2,'81d2b0ff-0060-42d6-8285-a1f25e7c4036'),
       ('d8c344d1-ddad-420f-ba71-d771d0b4b728',2,'81d2b0ff-0060-42d6-8285-a1f25e7c4036'),
       ('671135d3-4b5b-4ec1-85a5-a15ef9372f7e',1,'892f8371-20d5-4e97-8a39-ed24b3b9be98'),
       ('892f8371-20d5-4e97-8a39-ed24b3b9be98',2,'671135d3-4b5b-4ec1-85a5-a15ef9372f7e')
;
commit;