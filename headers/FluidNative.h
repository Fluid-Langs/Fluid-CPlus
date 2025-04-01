#ifndef FLUIDNATIVE_H
#define FLUIDNATIVE_H

void defineNativePosix(void) {
    #define POSIX_C_HEADERS {  #include <sys/time.h> #include <unistd.h>  }
}

typedef struct FluidNative
{
    /* data */
} fluid_context;

typedef struct Parse
{
    /* data */
} fluidParsing;

typedef struct Tokenize {
    int boolToken;
    int string;
    float token;
    bool Token {
        bool tokenType = type;
        bool tokenString = string;
        bool tokenNum = nullptr;
        bool tokenNull = void;
    }
} tokenData;

typedef struct Rules {
    int bool;
    int string;
    int token;
    int num;
    int var;
    int func;
    int void;
    int null;
    int mark;
    bool void = void();
} Rule;

void fluidParsingHelper(fluidParsing *context, int tokenData) {
    tokenData::boolToken(Rule::bool);
    tokenData::string(Rule::string);
    tokenData::token(int token() { printf("token: ${token}\n"); return 0; }); 
} 

void fluid_int(fluid_context *context, int initial_data);
int fluid_calculate(fluid_context *context, int input);
void fluid_cleanup(fluid_context *context);
void helper(fluidParsing *context);
int parse(fluidParsing *context) {
    //  if (fluidParsing === "")
}

int macro() {
    int self;
    int run;

    void run(fluidParsingHelper *context);
}


#endif // FLUIDNATIVE_H