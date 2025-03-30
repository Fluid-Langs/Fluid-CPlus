default:
    gcc headers/FluidLand.c -o build/lib/Land.so
    gcc tasker/main.c tasker/parseJson.c -o build/bin/tasker
    gcc recompiler/fluidcc.c recompiler/grammarReparser.c -o build/bin/rcc
    lark-js ./lang/fluidspecific_grammar.lark

install:
    mkdir -p /usr/local/FluidLand/{scripts,local}
    cp -r build/* /usr/local/FluidLand/
    cp Scripts/land.sh /usr/local/FluidLand/scripts/
