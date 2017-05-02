CREATE_DATABASE_and_connect = {
    # In the VM enter the psql prompt

    # create database name;
    """ create database fishies;"""
    
    # to connect to the database
    """\c fishies"""
    # or exit psql prompt and run `psql fishies`
}

CREATE_TABLE_AND_DECLARE_PRIMARY_KEYS = {
    """
    create table students (
        id serial primary key,
        name text,
        birthday date
    );
    """
    # an example insert into the above table 
    """ insert into students values ('This is text!'); """
    
    # Multi column primary key
    """
    create table postal_places (
        postal_code text,
        country text,
        name text,
        primary key (postal_code, country)    
    );
    """
}

DECLARE_RELATIONSHIPS = {
    # Declare certain values must relate to an id number etc
    # On Two separate tables where one id must correlate to another table to make sense,
    # Rather than add a non-existent id to a secondary table
    # eg. sku is stock unit
    """
    create table sales (            
        sku text references products,
        sale_date date,
        count integer
    );
    """
}
