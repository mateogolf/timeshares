# timeshares Repo
Individual Python Project during Coding Dojo Python
Key Features:
1.  Login/Registration for this web app
    -   Basic Login
    User Table
        first_name  VARCHAR(100)
        last_name   VARCHAR(100)
        email       VARCHAR(255) ***encrypt***
        password    VARCHAR(255) ***encrypt***
        admin       BOOLEAN===> True: Can add information to Tables: SourceType, Source, Currency, PropTypes
        created_at  DATETIME
        updated_at  DATETIME
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
        source      OnetoMany========>source_points (Interval deals in timeshares and multiple types of points?)
        trade/bank  TINYINT==>
            0: currency NOT related to points,
            1: TRADE: timeshare=>hotel points
                a timeshare from the related source can TRADE into this currency type to use at their hotels
            2: BANK: timeshare=>Resorts (Other timeshares)
                a timeshare from the related source can BANK into this currency type to use at their resorts

    -   Type of points:
        -   Marriott:
            -   MRP         (Hotel)
            -   VCP         (Resort/Other Timeshares)
        -   Starwood:
            -   SPG         (Hotel)
            -   SO          (Resort/Other Timeshares)
        -   Amex: points
        -   Interval: property and/or points
        -   United: miles
        -   Hawaiian: miles
        
    Account Table
        acct_nick   VARCHAR 
        username    VARCHAR ***encrypt***
        source      ManytoMany "accounts"===>Source()
        login_url   VARCHAR ***default is source's login page***
        total_pts   INT     ***Total points for this account***
        created_at  DATETIME
        updated_at  DATETIME
    
    Account_Points (Many to Many Table)
        points          INT
        type            OnetoMany===>Currency()
        availability    OnetoOne===>Availability() links the accounts' points to the timeshare and the year that it was banked
        exp_date        DATETIME
        account_id      OnetoMany===>Account()
        master_changed  BOOLEAN==>Warning that user updated the points amount and must update what points batch was used
        created_at      DATETIME
        updated_at      DATETIME

3.  Keep Track of the owned Timeshares (static)
    PropTypes Table
        name        VARCHAR===>color coded (Gold)
        rules       TEXT
        rules_url   VARCHAR==>Link to rules for given property type
        source      OnetoMany==>Source()
        created_at  DATETIME
        updated_at  DATETIME


    Property Table:
        name        VARCHAR
        <!-- source      OnetoMany==>Source() --> ***Not needed if in the type table***
        address     OneToMany===>Address()
        type        OnetoMany===>PropType() :***(Red,Silver,Platinum, Platinum, Gold+)***
        <!--DO the types in Interval help identify whether a property is annual/bi-annual?-->
        frequency   TINYINT()==>1: annual;2: bi-annual;
        isEven      BOOLEAN==>True-even year ***REQUIRED if frequency=2***
        isLockoff   BOOLEAN==>***True only possible for Starwood/Vistana ONLY option***
        trade_val   INT===>TOTAL points you get when traded for source's hotel system
        bank_val    INT===>TOTALpoints you get when banked for source's resort system (other timeshares)
        created_at  DATETIME
        updated_at  DATETIME

    PropertyValue:
        value       INT
        currency    OnetoMany===>Currency()
        isMain      BOOLEAN
        ***True-value is points from main lockoff***
        ***Fal se-value is points from studio lockoff***


4.  Keep Track of when points/timeshares expire (based on year and current reservations)
    -   Availability Table for timeshares available by year
        -   Using info in Timeshares table, generate entries in availability for next X years
        -   Status must be tracked, so you know what happened to the timeshare from which year

    Status Table - (Available,Traded,Banked,RESERVED)
        name        VARCHAR
        desc        TEXT ===>What can be done at each point

    Availability  Table (Available property for conversion and its status)
        property        OnetoMany===>Property()
        use_year        YEAR
        status          OnetoMany===>Status()
        created_at      DATETIME
        updated_at      DATETIME

    -   User's Totals: Sum of points based on all of the accounts for each user
    -   User's Points by Year: Sum all 


5.  Keep Track of currently booked reservations AND what if left available for this year and next
    -   Total points available this year, next year
