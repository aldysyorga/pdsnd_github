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
    cities = ['chicago', 'new york city', 'washington']
    while True:
        city = input('Please input desired city: \nAvailable option: chicago, new york city, washington\n')
        if city.lower() in cities:
            city = city.lower()
            print('You have selected {}, processing...\n'.format(city))
            break
        else:
            print('Unexpected input, please try again')

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    while True:
        month = input('Please input desired month: \nAvailable option : all, january, february, march, april, may, june\n')
        if month.lower() in months:
            print('You have selected {}, processing...\n'.format(month.upper()))
            month = months.index(month.lower()) + 1
            break
        elif month.lower() == 'all':
            month = month.lower()
            print('You have not selected particular month, processing {} dataset...\n'.format(month.upper()))
            break
        else:
            print('Unexpected input, please try again')


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while True:
        day = input('Please input desired day of week: \nAvailable option : all, monday, tuesday, wednesday, thursday, friday, saturday, sunday\n')
        if day.lower() in days:
            day = day.title()
            print('You have selected {}, processing...\n'.format(day.upper()))
            break
        elif day.lower() == 'all':
            day = day.lower()
            print('You have not selected particular day, processing {} dataset...\n'.format(day.upper()))
            break
        else:
            print('Unexpected input, please try again')

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
    df = pd.read_csv(CITY_DATA.get(city))
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        df = df[df['Month'] == month]
    if day != 'all':
        df = df[df['Day of Week'] == day]
        
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    popular_month = df['Month'].mode()[0]
    print('\nThe most common month is:')
    print(months[popular_month - 1].title())


    # TO DO: display the most common day of week
    popular_day = df['Day of Week'].mode()[0]
    print('\nThe most common day of week is:')
    print(popular_day.title())


    # TO DO: display the most common start hour
    popular_hour = df['Start Time'].dt.hour.mode()[0]
    print('\nThe most common start hour is:')
    print(popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('\nThe most commonly used start station is:')
    print(popular_start_station.title())


    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('\nThe most commonly used end station is:')
    print(popular_end_station.title())

    
    # TO DO: display most frequent combination of start station and end station trip
    df['Start-End Station'] = df['Start Station'] + ' - ' + df['End Station']
    popular_start_end_station = df['Start-End Station'].mode()[0]
    print('\nThe most frequent combination of start station and end station trip is:')
    print(popular_start_end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('\nTotal travel time is (in seconds):')
    print(total_travel_time)


    # TO DO: display mean travel time
    total_travel_time = df['Trip Duration'].mean()
    print('\nAverage travel time is (in seconds):')
    print(total_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        user_type_count = df.groupby(['User Type']).count().iloc[:, 0]
        print('\nCount of user type:')
        print(user_type_count)


        # TO DO: Display counts of gender
        gender_count = df.groupby(['Gender']).count().iloc[:, 0]
        print('\nCount of gender:')
        print(gender_count)
    except KeyError:
        print('\nGender data is NOT AVAILABLE for this dataset')


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        min_year_count = df['Birth Year'].min()
        print('\nEarliest year of birth is:')
        print(int(min_year_count))

        max_year_count = df['Birth Year'].max()
        print('\nMost recent year of birth is:')
        print(int(max_year_count))

        common_year_count = df['Birth Year'].mode()[0]
        print('\nMost common year of birth is:')
        print(int(common_year_count))
    except KeyError:
        print('\nBirth year data is NOT AVAILABLE for this dataset')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        """ Prompt if the user wants to see raw data, 5 rows at a time  as specified in project rubrics"""
        run_count = 0
        while True:
            data_display = input('\nWould you like to see the data? Enter yes or no.\n')
            if data_display.lower() == 'yes':
                first_row = run_count * 5
                last_row = first_row + 5
                print(df[first_row:last_row])
                run_count += 1
            elif data_display.lower() == 'no':
                break
            else:
                print('Invalid input')

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
