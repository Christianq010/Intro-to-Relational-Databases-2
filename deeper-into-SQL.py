# coding=utf-8
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

LEFT_JOIN = {
    # Suppose that we want to know how many times we have sold each product. In other words, for each sku value in the products table, we want to know the number of times it occurs in the sales table.
    # This query will give us a row for every product in the products table, even the ones that have no sales in the sales table.
    # We’re using count(sales.sku) instead of count(*). This means that the database will count only rows where sales.sku is defined, instead of all rows.
    # We’re using a left join instead of a plain join.

    """
    select products.name, products.sku, count(sales.sku) as num
        from products left join sales
        on products.sku = sales.sku
    group by products.sku;
    """
# -- Here are two tables describing bugs found in some programs.
# -- The "programs" table gives the name of each program and the files
# -- that it's made of.  The "bugs" table gives the file in which each
# -- bug was found.
# --
# -- create table programs (
# --    name text,
# --    filename text
# -- );
# -- create table bugs (
# --    filename text,
# --    description text,
# --    id serial primary key
# -- );
# --
# -- The query below is intended to count the number of bugs in each
# -- program. But it doesn't return a row for any program that has zero
# -- bugs. Try running it as it is.  Then change it so that the results
# -- will also include rows for the programs with no bugs.  These rows
# -- should have a 0 in the "bugs" column.

    """
    select programs.name, count(*) as num
       from programs join bugs
            on programs.filename = bugs.filename
       group by programs.name
       order by num;
    """
    
    # Answer
    
    """
    select programs.name, count(bugs.filename) as num
       from programs left join bugs
         on programs.filename = bugs.filename
       group by programs.name
       order by num;
    """

}