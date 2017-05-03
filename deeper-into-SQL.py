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

FOREIGN_KEYS = {
    # The keys reference to the primary key of a table
    # Table 1

    """
    create table students (
    id serial primary key,
    name text
    );
    """

    # Table 2
    """
    create table courses (
    id text primary key,
    name text
    );
    """
    
    # Table that references with foreign key  
    """
    create table grades (
    student integer references students (id),
    course text references courses (id),
    grade text
    );
    """

}

#
# Roommate Finder v0.9
#
# This query is intended to find pairs of roommates.  It almost works!
# There's something not quite right about it, though.  Find and fix the bug.
#

QUERY = '''
select a.id, b.id, a.building, a.room
       from residences as a, residences as b
 where a.building = b.building
   and a.room = b.room
 # and a.id < b.id   
 order by a.building, a.room;
'''

#
# To see the complete residences table, uncomment this query and press "Test Run":
#
# QUERY = "select id, building, room from residences;"
#
