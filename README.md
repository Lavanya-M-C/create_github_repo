#INSTALL:

      git clone "https://github.com/Lavanya-M-C/create_github_repo.git"
      cd create_github_repo
      pip install -r requirements.txt
      touch .env
      Then open the .env file and store your folder_path, github access_token & github username. Use the provided format at the bottom of this README.
      source ~/.my_custom_commands.sh

#USAGE:

To run the script type in 'create <name of your folder>'

#.env FILE FORMAT:

      FOLDERPATH="your-folder-path"
      GITHUB_ACCESSTOKEN="your-github-accesstoken"
      GITHUB_USERNAME="your-github-username"

#HOW TO GENERATE GITHUB ACCESS TOKEN:

      Go to settings->Developer settings->Personal access tokens
      Then generate one access token with desired scopes
      Then copy the access token before changing the tab
