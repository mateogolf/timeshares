# timeshares Repo
Individual Python Project during Coding Dojo Python
Key Features:
1.  Login/Registration for this web app
    -   Basic Login
    -   Forgot Username - Security Question to provide username
    -   Reset Password - send email with password reset link

2.  Keep Track of all relevant accounts and their points
    Address Table
        address1
        address2
        apt_num
        city
        state
        zip
    SourceType Table (Resort/Hotel, Credit Card, Trading Service, Airline)
        name        VARCHAR
        desc        VARCHAR
        hasProperties BOOLEAN ===>Source sells/deals timeshares
        
    Source Table (Marriott, Starwood, Amex, Interval, United, Hawaiian)
        name        VARCHAR
        description VARCHAR
        login_URL   VARCHAR
        type_id     OneToMany ==========>SourceType()
        exp_Rules   TEXT=========>Rules on Expiration of points/property
        notes       TEXT
        trade_by    DATETIME===>Deadline for when a timeshare must trade into these points
        bank_by     DATETIME===>Deadline for when a timeshare must bank into these points
        created_at  DATETIME
        updated_at  DATETIME
        
    
    Currency Table
        abrev       VARCHAR====>(MRP)
        name        VARCHAR====>(Marriott Reward Points)
        <!-- trade_date  DATETIME===>Deadline for when a timeshare must trade into these points -->
        duration    ==>How long these points stay valid
        source      ManytoMany========>source_points (Interval deals in timeshares and multiple types of points?)
        trade/bank  TINYINT==>
            0: currency NOT related to points,
            1: TRADE: timeshare=>hotel points
                a timeshare from the related source can TRADE into this currency type to use at their hotels
            2: BANK: timeshare=>Resorts (Other timeshares)
                a timeshare from the related source can BANK into this currency type to use at their resorts

    -   Type of points:
        -   Marriott:
            -   MRP         (Hotel)
            -   VCP         (Resort)
        -   Starwood:
            -   SPG         (Hotel)
            -   SO          (Resort)
        -   Amex: points
        -   Interval: property and/or points
        -   United: miles
        -   Hawaiian: miles
        
    Account Table
        acct_nick   VARCHAR
        username    VARCHAR
        source      ManytoMany "accounts"===>Source()
        login_url   VARCHAR <!--default is source's login page-->
        created_at  DATETIME
        updated_at  DATETIME
    
    Account_Points (Many to Many Table)
        type        OnetoMany===>Currency()
        points      INT
        exp_date    DATETIME
        account_id  OnetoMany===>Account()
        created_at  DATETIME
        updated_at  DATETIME

3.  Keep Track of the owned Timeshares (static)

    Property Table:
        name        VARCHAR
        source      OnetoMany==>Source()
        address     OneToMany===>Address()
        interval    OnetoMany===>PropType() :(Red,Silver,Odd Year, Platinum Odd & Even, Gold+)
        <!--WHAT are the different types that are listed here?-->
        <!--DO the types in Interval help identify whether a property is annual/bi-annual?-->
        frequency   TINYINT()==>1: annual;2: bi-annual; 3: tri-annual
        trade_val   INT===>points you get when traded for source's hotel points
        bank_val    INT===>points you get when banked for source's resort system (other timeshares)
        created_at  DATETIME
        updated_at  DATETIME


4.  Keep Track of when points/timeshares expire (based on year and current reservations)
    -   User's Totals: Sum of points based on all of the accounts for each user
    -   User's Points by Year: Sum all 


5.  Keep Track of currently booked reservations AND what if left available for this year and next
    -   Total points available this year, next year
