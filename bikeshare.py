import time
import pandas as pd
import numpy as np

"""List the cities where data is available"""
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

"""Simulate some refactoring part one"""
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    """If the user enters a city which is not part of our project, there is a message and the question is asked again as long as the user enters one of the relevant cities"""
    cities = ['chicago', 'new york city', 'washington']
    while True:
        city = input("Please enter the city (chicago, new york city, washington) ").lower()
        if city in cities:
            break
        else:
            print("This city is not in our project")  
    
    """If the user enters a month which is not part of our project, there is a message and the question is asked again as long as the user enters one of the relevant             months"""
    months = ['january', 'february', 'march', 'april', 'may', 'june','all']  
    while True:
        month = input("PLease enter the month (january, february, ..., june or all) ").lower()
        if month in months:
            break
        else:
            print("This month is not in our project")
    """If the user enters a day which is not part of our project, there is a message and the question is asked again as long as the user enters one of the relevant days"""
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']         
    while True:
        day = input('Please enter the day (sunday, monday, tuesday, wednesday, thursday, friday, saturday, all) ').lower()
        if day in days:
            break
        else:
            print ('This month is not in our project')
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    """load data file into a dataframe"""
    df = pd.read_csv(CITY_DATA[city])

    """convert the Start Time column to datetime"""
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    """extract month and day of week from Start Time to create new columns"""
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    """include also the hours for the specific question"""
    df['hour'] = df['Start Time'].dt.hour

    """filter by month if applicable"""
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        """filter by month to create the new dataframe"""
        df = df[df['month'] == month]

    """filter by day of week if applicable"""
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    print(df.head())
    return df

"""Simulate some refacturing part two"""
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('Most common month: ', most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('Most common day of the week: ', most_common_day)

    # TO DO: display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print('Most common start hour: ', most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station :", most_start_station)

    # TO DO: display most commonly used end station
    most_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station :", most_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['most_start_end'] = df['Start Station'] + df['End Station']
    print('The most frequent combination of start station and end station trip is {}'.format((df['most_start_end'].mode()[0])))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time :", total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time :", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_counts = df['User Type'].value_counts()
    print("Counts user types: ", user_counts)

    # TO DO: Display counts of gender
    """There is no data for Gender for Washington. If Washington is chosen, print a message to point this out"""
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print("Counts gender: ", gender_counts)
    else:
        print('There is no Gender Data for this city.')

    # TO DO: Display earliest, most recent, and most common year of birth
    """There is no data for Birth Year for Washington. If Washington is chosen, print a message to point this out"""
    if 'Birth Year' in df.columns:
        birth_year = df['Birth Year']
        # the most common birth year
        most_common_year = birth_year.mode()[0]
        print("The most common birth year:", most_common_year)
        # the most recent birth year
        most_recent = birth_year.max()
        print("The most recent birth year:", most_recent)
        # the most earliest birth year
        earliest_year = birth_year.min()
        print("The most earliest birth year:", earliest_year)
    else:
        print('There is no Data for Birth Year for this city.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
"""Simulat refactor part three"""
"""The user is asked if some raw data should be displayed and if yes then this is displayed and the user is asked if addtional five rows should be displayed and so on until no is entered"""
def raw_data(df):
    next_rows = input('\nWould you like to see first 5 rows of raw data? Please enter yes or no ').lower()
    if next_rows == 'yes':
        i = 0
        while True:
            print(df.iloc[i:i+5])
            i += 5
            another_five_rows = input('Would you like to see more data? Please enter yes or no: ').lower()
            if another_five_rows != 'yes':
                break

"""Adding the raw_data function to the main function"""
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


