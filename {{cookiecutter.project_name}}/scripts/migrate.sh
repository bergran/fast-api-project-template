input_variable=$1

# Refactor this pls! :D
if [ $input_variable == "--help" ] || [ $input_variable == '-h' ]
    then
        echo "This is a help to use migrate command"
        echo "--help or -h will show help"
        echo "Also you can use this input to introduce revision or head"
else
    PYTHONPATH=.; alembic upgrade $1
fi