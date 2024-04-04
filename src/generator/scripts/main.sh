# TODO tab completition?
alias pq=my-password-please

my-password-please() {
    if [ "$#" -ne 1 ]; then
        echo "Error: Please provide arguments."
        echo "Usage: $0 <platform>"
        return 1
    fi

    echo "Generating your password for platform: $1"

    python3 "$HOME/vs/password-generator/src/generator/main.py" $1
}
