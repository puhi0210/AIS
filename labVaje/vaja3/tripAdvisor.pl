:- include('travel_agent.pl').

% hi/0
% Displays a greeting.
hi:-
    write('Welcome to Tripadvisor, for more information write "help.".').

% help/0
% Displays a list of available functions and their descriptions.
help:-
    nl,
    write('Available Functions:'), nl,
    write('-------------------'), nl,
    write('1. suggest_city'), nl,
    write('   - Description: Suggests cities based on your preferred type of transport and budget preference.'), nl, nl,
    write('2. suggest_landmark'), nl,
    write('   - Description: Provides a list of top landmarks in a specified city and suggests a related travel guide.'), nl, nl,
    write('3. suggest_restaurant'), nl,
    write('   - Description: Recommends restaurants in a specified city based on cuisine preference, price range, and minimum rating.'), nl, nl,
    write('4. help'), nl,
    write('   - Description: Displays this help message with a list of available functions and their descriptions.'), nl, nl.

% suggest_city/0
% Suggests cities based on your preferred type of transport and budget preference.
suggest_city:-
    nl,
    write('What type of transport do you prefer (plane/other)? '), nl,
    read(Transport), nl,
    write('Do you prefer a low or high budget trip (low/trip)? '), nl,
    read(Budget), nl,
    write('You can travel to:'), nl, nl,
    find_city(Transport, Budget).

% find_city/2
% Finds and displays cities matching the specified budget and transport type.
find_city(Transport, Budget):-
    transport(City, Transport),
    cost(City, Budget),
    write(City), nl,
    fail.

% suggest_landmark/0
suggest_landmark:-
    nl,
    write('Enter the city you are interested in: '), nl,
    read(City), nl,
    write('How many landmarks would you like to see (1-5)? '), nl,
    read(N), nl,
    findnsols(N, Landmark, landmark(City, Landmark), Landmarks),
    travel_guide(City, BookTitle, Author),
    write('Top landmarks:'), write(Landmarks), nl, nl,
    write('For more information, check out the travel guide: '), write(BookTitle), write(' by '), write(Author), nl.

suggest_restaurant:- 
    nl,
    write('Enter the city you are looking for restaurants in: '), nl,
    read(City), nl,
    write('Enter your preferred cuisine: '), nl,
    read(Cuisine), nl,
    write('Enter the maximum price range (1, 2 or 3): '), nl,
    read(Price), nl,
    write('Enter the minimum average rating (example: 4.5): '), nl,
    read(Rating), nl,
    findall(Restaurant,
        (   
        restaurant(City, Restaurant),
        cuisine(Restaurant, Cuisine),
        price_range(Restaurant, P),
        P=< Price,
        rating(Restaurant, R),
        R >= Rating
        ),
        Restaurants),
    write('Suggested restaurants:'),write(Restaurants), nl.