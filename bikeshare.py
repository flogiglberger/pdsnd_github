# Welcome to the project Explore US Bikeshare Data

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    while True:
            city = input('Choose between chicago, new york city, and washington: ').lower()
            if city not in ['chicago', 'new york city', 'washington']:
                print('\nThis city is not available. Please try again!\n')
            else:
                break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
            month = input('Choose a month (all, january, february, ... , june): ').lower()
            if month not in ['all', 'january', 'february', 'march', 'april', 'may','june']:
                print('This month is not available. Please try again!\n')
            else:
                break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
            day = input('Choose a day (all, monday, tuesday, ... sunday): ').lower()
            if day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday', 'sunday']:
                print('This is not a day of the week. Please try again!\n')
            else:
                break

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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    most_month = months[df['month'].mode()[0] -1]
    print('Most common month: ', most_month)

    # TO DO: display the most common day of week
    most_day = df['day_of_week'].mode()[0]
    print('Most common day of the week: ', most_day.lower())

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_hour = df['hour'].mode()[0]
    print('Most common start hour: ', most_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start_station = df['Start Station'].mode()[0]
    print('Most commonly used start station: ', most_start_station)

    # TO DO: display most commonly used end station
    most_end_station = df['End Station'].mode()[0]
    print('Most commonly used end station: ', most_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_combination = ('From ' + df['Start Station'] + ' to ' + df['End Station']).mode()[0]
    print('Most frequent combination of start station and ende station: ', most_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is {} seconds.\nThat are {} hours or {} days. '.format(total_travel_time, total_travel_time/3600, total_travel_time/(3600 * 24)))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('\nThe mean travel time is {} seconds.\nThat are {} hours.'.format(mean_travel_time, mean_travel_time/3600))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_types = df['User Type'].value_counts()
    print('The counts of user types are:\n', count_user_types)

    # TO DO: Display counts of gender
    if city != 'washington':
        count_gender = df['Gender'].value_counts()
        print('The counts gender are:\n', count_gender)
    else:
        print('Gender data is not available for washington.')

    # TO DO: Display earliest, most recent, and most common year of birth
    if city != 'washington':
        earliest_by = int(min(df['Birth Year']))
        most_recent_by = int(max(df['Birth Year']))
        most_common_by = int(df['Birth Year'].mode()[0])
        print('The earliest year of birt: {}\nThe most recent year of birth: {}\nThe most common year of birth: {} '.format(earliest_by, most_recent_by, most_common_by))
    else:
        print('Year of birth data is not available for washington.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    """Displays 5 lines of raw data every time the user inputs 'yes'."""

    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()

    if view_data == 'yes':

        start_loc = 0
        view_display = 'yes'

        while (view_display != 'no'):

            print(df.iloc[start_loc:start_loc + 5])
            start_loc += 5
            view_display = None

            while (view_display not in ['yes', 'no']):
                view_display = input("Do you wish to continue?: ").lower()

    else:
        print('No individual trip data necessary.')


def main():
    """Calls function after function in order to run the project"""
    
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
