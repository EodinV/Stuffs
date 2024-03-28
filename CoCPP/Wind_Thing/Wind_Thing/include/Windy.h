#if !defined(WINDY)
#define WINDY

#define N 0
#define NE 1
#define E 2
#define SE 3
#define S 4
#define SW 5
#define W 6
#define NW 7
#define BAROA SDA
#define BAROL SCL
#define DHTPIN 9
#define DHTTYPE DHT11
#define LEDN 10
#define LEDNE 11
#define LEDE 12
#define LEDSE 13
#define LEDS 14
#define LEDSW 15
#define LEDW 16
#define LEDNW 17
int chill = 0;
int bearing = 0;
DHT dht(DHTPIN,DHTTYPE);



int corr = 0;

/**
 * @brief collect temperature from DHT via serial communication
 * 
 * @return int 
 */
int temp()
{

}

/**
 * @brief collect data from barometer via I2C.
 * 
 * @return int 
 */
int barometer()
{

}

/**
 * @brief //use hygrometer and barometer to adjust windchill factor. shoud return an int.
 * 
 * @return int 
 */
int correction()
{

}

/**
 * @brief //calculate windchill to determine approximate windspeed
 * 
 * @return int 
 */
int windchill()
{

}

/**
 * @brief //compare temperatures to determine/calculate wind direction
 * 
 * @return int 
 */
int direction()
{

}

/**
 * @brief setup pins and baudrate
 * 
 */
void setup()
{

}

/**
 * @brief use functions in a loop to do ehat we want done.
 * 
 */
void loop()
{
    

}

#endif // WINDY
