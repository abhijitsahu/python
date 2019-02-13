import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def validate_city(city):
    """
    validate city

    Inputs:
        (str) city - name of the city to analyze
    Returns:
        True : If input is a valid city
        False : Otherwise
    """
    city = city.lower()
    if (city == 'chicago') or (city == 'new york city') \
            or (city == 'washington'):
        # It's a valid input so return true
        return True
    else:
        # It's a invalid input so return false
        return False


def validate_month(month):
    """
    validate month

    Inputs:
        (str) city - name of the month to analyze
    Returns:
        True : If input is a valid month
        False: Otherwise
    """
    month = month.lower()
    if (month == 'january') or (month == 'february') \
            or (month == 'march') or (month == 'april') \
            or (month == 'may') or (month == 'june') \
            or (month == 'all'):
        # It's a valid input so return true
        return True
    else:
        # It's a invalid input so return false
        return False


def validate_day_of_week(day):
    """
    validate day of week

    Inputs:
        (str) day - day of week
    Returns:
        True : If input is a valid city
        False: Otherwise
    """
    day = day.lower()
    if (day == 'sunday') or (day == 'monday')\
            or (day == 'tuesday') or (day == 'wednesday')\
            or (day == 'thursday') or (day == 'friday')\
            or (day == 'saturday') or (day == 'all'):
        # It's a valid input so return true
        return True
    else:
        # It's a invalid input so return false
        return False


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city  - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no
                      month filter
        (str) day   - name of the day of week to filter by, or "all" to apply
                      no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington).
    # HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Enter city(string): ")
        if validate_city(city):
            city = city.lower()
            break
        else:
            print(' ERROR: Invalid input:')
            print(' Please enter "chicago", "new york city" OR "washington"')

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Enter Month(string):')
        if validate_month(month):
            month = month.lower()
            break
        else:
            print(' ERROR: Invalid input:')
            print(' Please enter "January","February","March" ... OR "June"')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Enter day of week(string):')
        if validate_day_of_week(day):
            day = day.lower()
            break
        else:
            print(' ERROR: Invalid input:')
            print(' Please enter "Monday", "Tuesday" , ..."Sunday"')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if \
    applicable.

    Args:
        (str) city  - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply \
                      no month filter
        (str) day   - name of the day of week to filter by, or "all" to apply \
                     no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['hour'] = pd.DatetimeIndex(df['Start Time']).hour
    df['month'] = pd.DatetimeIndex(df['Start Time']).month
    df['day_of_week'] = pd.DatetimeIndex(df['Start Time']).weekday_name

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

    # display the most common month
    common_month = df.loc[:, 'month'].mode()[0]
    print('most common month : ', common_month)

    # display the most common day of week
    common_day = df.loc[:, 'day_of_week'].mode()[0]
    print('most common day_of_week : ', common_day)

    # display the most common start hour
    popular_hour = df.loc[:, 'hour'].mode()[0]
    print('most common start hour : ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_stn = df['Start Station'].mode()[0]
    print('most commonly used start station : ', most_common_start_stn)

    # display most commonly used end station
    most_common_end_stn = df['End Station'].mode()[0]
    print('most commonly used end station : ', most_common_end_stn)

    # display most frequent combination of start station and end station trip
    df['Combine Start End Station'] = df['Start Station'] + ' <==> ' + \
                                                    df['End Station']
    most_common_end_stn = df['Combine Start End Station'].mode()[0]
    print('most frequent combination stations: ', most_common_end_stn)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    if 'Trip Duration' in df.columns:
        print('\nCalculating Trip Duration...\n')
        start_time = time.time()

        # display total travel time
        total_travel_time = df['Trip Duration'].sum()
        print('total travel time : ', total_travel_time)

        # display mean travel time
        travel_mean_time = df['Trip Duration'].mean()
        print('mean travel time : ', travel_mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    if 'User Type' in df.columns:
        # Display counts of user types
        user_types_cnt = df['User Type'].value_counts()
        print('*************************')
        print('counts of user types : ')
        print('*************************')
        print(user_types_cnt)

    if 'Gender' in df.columns:
        # Display counts of gender
        gender_cnt = df['Gender'].value_counts()
        print('*************************')
        print('counts of gender : ')
        print('*************************')
        print(gender_cnt)

    if 'Birth Year' in df.columns:
        # Display earliest, most recent, and most common year of birth
        print('*************************')
        print('earliest year of birth : ', df['Birth Year'].min())
        print('most recent year of birth : ', df['Birth Year'].max())
        print('most common year of birth : ', df['Birth Year'].mode()[0])
        print('*************************')
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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
