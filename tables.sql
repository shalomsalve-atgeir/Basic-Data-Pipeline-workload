-- CREATE DATABASE basic_DataPipeline;

USE basic_DataPipeline;

-- Creating tables

-- RAW CAMPAIGNS
CREATE TABLE raw_campaigns (
    campaign_id VARCHAR(40),
    campaign_name VARCHAR(100),
    campaign_type VARCHAR(100),
    start_date DATE,
    end_date DATE,
    target_segment VARCHAR(100),
    budget DECIMAL(12,2),
    impressions DECIMAL(12,0),
    clicks DECIMAL(12,0),
    conversions DECIMAL(12,0),
    conversion_rate DECIMAL(6,2),
    roi DECIMAL(10,2)
);

-- RAW CUSTOMERS
CREATE TABLE raw_customers (
    customer_id VARCHAR(40),
    full_name VARCHAR(100),
    age INT,
    gender VARCHAR(20),
    email VARCHAR(100),
    phone VARCHAR(50),
    street_address VARCHAR(100),
    city VARCHAR(100),
    state VARCHAR(50),
    zip_code VARCHAR(10),
    registration_date DATE,
    preferred_channel VARCHAR(50)
);


-- RAW CUSTOMER REVIEWS
CREATE TABLE raw_customer_reviews (
    review_id VARCHAR(40),
    customer_id VARCHAR(40),
    product_name VARCHAR(100),
    product_category VARCHAR(100),
    full_name VARCHAR(100),
    transaction_date DATE,
    review_date DATE,
    rating INT,
    review_title VARCHAR(100),
    review_text TEXT
);

-- RAW INTERACTIONS
CREATE TABLE raw_interactions (
    interaction_id VARCHAR(40),
    customer_id VARCHAR(40),
    channel VARCHAR(50),
    interaction_type VARCHAR(50),
    interaction_date DATETIME,
    duration DECIMAL(10,2),
    page_or_product VARCHAR(100),
    session_id VARCHAR(100)
);

-- RAW SUPPORT TICKETS
CREATE TABLE raw_support_tickets (
    ticket_id VARCHAR(40),
    customer_id VARCHAR(40),
    issue_category VARCHAR(50),
    priority VARCHAR(50),
    submission_date DATE,
    resolution_date DATE,
    resolution_status VARCHAR(50),
    resolution_time_hours DECIMAL(10,2),
    customer_satisfaction_score DECIMAL(5,2),
    notes TEXT
);

-- RAW TRANSACTIONS
CREATE TABLE raw_transactions (
    transaction_id VARCHAR(40),
    customer_id VARCHAR(40),
    product_name VARCHAR(50),
    product_category VARCHAR(50),
    quantity DECIMAL(10,2),
    price DECIMAL(10,2),
    transaction_date DATE,
    store_location VARCHAR(50),
    payment_method VARCHAR(50),
    discount_applied DECIMAL(10,2)
);

-- AUDIT LOG 
CREATE TABLE audit_log (
    audit_id INT AUTO_INCREMENT PRIMARY KEY,
    process_name VARCHAR(50),
    file_name VARCHAR(100),
    table_name VARCHAR(100),
    start_time DATETIME,
    end_time DATETIME,
    rows_loaded INT,
    status VARCHAR(20)
);

