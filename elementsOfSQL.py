# Try out this query! You'll see the results below.
# You'll be seeing many more pages like this in the rest of this lesson.
# For now, just test it out.

QUERY = {

    # Search for a gorilla named Max
    '''
select name, birthdate from animals where species = 'gorilla' and name = 'Max';
    ''',

    # Return all animals that are not gorillas or animals named Max
    '''
select name from animals where not (species = 'gorilla' or name = 'Max'); 
    ''',
    '''
select name from animals where species != 'gorilla' and name != 'Max'; 
    '''
    # Comparision Operators 
    '''
select name from animals where species = 'llama' and birthdate >= '1995-01-01' and birthdate <= '1998-12-31';
    
    '''
}

Experimental_Queries = {

    # Uncomment one of these QUERY variables at a time and use "Test Run" to run it.
    # You'll see the results below.  Then try your own queries as well!
    #

    # QUERY = "select max(name) from animals;"

    # QUERY = "select * from animals limit 10;"

    # QUERY = "select * from animals where species = 'orangutan' order by birthdate;"

    # QUERY = "select name from animals where species = 'orangutan' order by birthdate desc;"

    # QUERY = "select name, birthdate from animals order by name limit 10 offset 20;"

    # QUERY = "select species, min(birthdate) from animals group by species;"

    # QUERY = '''
    # select name, count(*) as num from animals
    # group by name
    # order by num desc
    # limit 5;
    # '''

    #
    # Write a query that returns all the species in the zoo, and how many animals of
    # each species there are, sorted with the most populous species at the top.
    #
    # The result should have two columns:  species and number.
    #
    # The animals table has columns (name, species, birthdate) for each individual.

    # Query = "select * as num, species from animals group by species order by num desc; "

}

Adding_rows = {
    #
    # Insert a newborn baby opossum into the animals table and verify that it's
    # been added. To do this, fill in the rest of SELECT_QUERY and INSERT_QUERY.
    #
    # SELECT_QUERY should find the names and birthdates of all opossums.
    #
    # INSERT_QUERY should add a new opossum to the table, whose birthdate is today.
    # (Or you can choose any other date you like.)
    #
    # The animals table has columns (name, species, birthdate) for each individual.
    #

    # SELECT_QUERY = '''
    # select ... where ...;
    # '''

    # Find the possums already in the table and add the newborn possum to the table

    # INSERT_QUERY = '''
        #  insert into animals (na, species, birthdate)
        #  values ('Wibble', 'opossum', '2014-11-14');
    # or
        #  insert into animals
        #   values ('Wibble', 'opossum', '2014-11-14');
    # '''

}

join_tables_and_find = {
    # Find all the individual animals that eat Fish

    # The animals table has columns (name, species, birthdate) for each individual.
    # The diet table has columns (species, food) for each food that a species eats.
    #

    # QUERY = '''
    # Answer One
    # select animals.name from animals join diet on animals.species and diet.species where food = 'fish';
    # Answer Two
    # select name from animals, diet where animals.species = diet.species and diet.food = 'fish';
    # '''
}

having_clause = {
    #
    # Find the one food that is eaten by only one animal.
    #
    # The animals table has columns (name, species, birthdate) for each individual.
    # The diet table has columns (species, food) for each food that a species eats.
    #

    # QUERY = '''
    # select select food, count(animals.name) as num
    #    from diet join animals
    #    on diet.species = animals.species
    #    group by food
    #    having num = 1
    # '''
    # or
    # select food, count(animals.name) as num
    #        from diet, animals
    #        where diet.species = animals.species
    #        group by food
    #        having num = 1

}

more_joins = {
    #
    # List all the taxonomic orders, using their common names, sorted by the number of
    # animals of that order that the zoo has.
    #
    # The animals table has (name, species, birthdate) for each individual.
    # The taxonomy table has (name, species, genus, family, t_order) for each species.
    # The ordernames table has (t_order, name) for each order.
    #
    # Be careful:  Each of these tables has a column "name", but they don't have the
    # same meaning!  animals.name is an animal's individual name.  taxonomy.name is
    # a species' common name (like 'brown bear').  And ordernames.name is the common
    # name of an order (like 'Carnivores').

    # QUERY = '''
    #     select ordernames.name, count(*) as num
    #       from animals, taxonomy, ordernames
    #       where animals.species = taxonomy.name
    #         and taxonomy.t_order = ordernames.t_order
    #       group by ordernames.name
    #       order by num desc
    # '''
}