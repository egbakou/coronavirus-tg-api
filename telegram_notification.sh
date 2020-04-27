#!/bin/sh

##########################################################################
# Note: you must have set up your Travis CI environment variables for this
# project to include both TELEGRAM_TOKEN and TELEGRAM_CHAT_ID
# For more details, see the Telegram documentation at:
#   - https://core.telegram.org/bots/api
# and the blog posts at:
#   - https://ansonvandoren.com/posts/telegram-notification-on-deploy/
#   - https://ansonvandoren.com/posts/travis-telegram-integration/
##########################################################################

# Get the token from Travis environment vars and build the bot URL:
BOT_URL="https://api.telegram.org/bot${TELEGRAM_TOKEN}/sendMessage"

# Set formatting for the message. Can be either "Markdown" or "HTML"
PARSE_MODE="Markdown"

# Use built-in Travis variables to check if all previous steps passed:
if [ $TRAVIS_TEST_RESULT -ne 0 ]; then
    build_status="Failed 😩 😩 😩"
else
    build_status="succeeded 😎 😎 😎 "
fi

# Define send message function. parse_mode can be changed to
# HTML, depending on how you want to format your message:
send_msg () {
    curl -s -X POST ${BOT_URL} -d chat_id=$TELEGRAM_CHAT_ID \
        -d text="$1" -d parse_mode=${PARSE_MODE}
}

# Send message to the bot with some pertinent details about the job
# Note that for Markdown, you need to escape any backtick (inline-code)
# characters, since they're reserved in bash
send_msg "
Travis Build **${build_status}!**
$TITLE

$TEXT

\`Repository:  ${TRAVIS_REPO_SLUG}\`
\`Branch or Tag: ${TRAVIS_BRANCH}\`
[Repo on Github](https://github.com/${TRAVIS_REPO_SLUG})
"