CREATE TABLE "patient" (
	"patient_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"name" varchar (255) NOT NULL,
	"date_of_birth" datetime NOT NULL,
	"city" varchar (255),
	"state" varchar (255),
	"country" varchar (255),
	"street_address" varchar (255),
	"telephone" varchar (255)
);

CREATE TABLE "symptom" (
	"symptom_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"name" varchar (255) NOT NULL,
	"description" boolean NOT NULL,
	"has_duration" boolean DEFAULT false NOT NULL,
	"has_bodypart" boolean DEFAULT false NOT NULL, 
	"has_severity"  boolean DEFAULT false NOT NULL,
	"has_character"  boolean DEFAULT false NOT NULL
);

CREATE TABLE "localization" (
	"locale_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"name" varchar (255) NOT NULL
);

CREATE TABLE "disease" (
	"icd_code" varchar(10) NOT NULL PRIMARY KEY,
	"name" varchar (255) NOT NULL,
	"description" text
);

CREATE TABLE "diseasepatients" (
	"icd_code" varchar(10) NOT NULL,
	"patient_id" integer NOT NULL,
	CONSTRAINT fk_disease
		FOREIGN KEY("icd_code") REFERENCES "disease" ("icd_code"),
	CONSTRAINT fk_patient
		FOREIGN KEY("patient_id") REFERENCES "patient" ("patient_id")
);

CREATE TABLE "diseasesymptoms" (
	"icd_code" varchar(10) NOT NULL,
	"symptom_id" integer NOT NULL,
	CONSTRAINT fk_disease
		FOREIGN KEY("icd_code") REFERENCES "disease" ("icd_code"),
	CONSTRAINT fk_symptom
		FOREIGN KEY("symptom_id") REFERENCES "symptom" ("symptom_id")
);

CREATE TABLE "observation" (
	"observation_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"patient_id" integer NOT NULL,
	"symptom_id" integer NOT NULL,
	"symptom_start_time" datetime NOT NULL,
	"duration" integer,
	"severity" integer,
	"description" text,
	"character" varchar(255),
	"timing" varchar(50),
	"locale_id"	integer,
	"log_time" datetime NOT NULL,
	CONSTRAINT fk_patient
		FOREIGN KEY("patient_id") REFERENCES "patient" ("patient_id"),
	CONSTRAINT fk_symptom
		FOREIGN KEY("symptom_id") REFERENCES "symptom" ("symptom_id")
);

