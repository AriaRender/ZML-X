#!/usr/bin/env python3
YT_HELP_MESSAGE = """
<b><u>Mirror</u></b>:
<code>/{cmd}</code> link
Or reply to the link with <code>/{cmd}</code>

<b>Rename</b>: -n
<code>/{cmd}</code> link -n New_Name
<b><u>Note</u></b>: Don't add file extension

<b>Quality Buttons</b>: -s
Incase default quality added from yt-dlp options using format option and you need to select quality for specific link or links with multi links feature.
<code>/{cmd}</code> link -s

<b>Zip</b>: -z password
<code>/{cmd}</code> link -z (zip)
<code>/{cmd}</code> link -z password (zip password protected)

<b>Options</b>: -opt
<code>/{cmd}</code> link -opt playliststart:^10|fragment_retries:^inf|matchtitle:S13|writesubtitles:true|live_from_start:true|postprocessor_args:{{"ffmpeg": ["-threads", "4"]}}|wait_for_video:(5, 100)
<b><u>Note</u></b>: Add `^` before integer or float, some values must be numeric and some string.
Like playlist_items:10 works with string, so no need to add `^` before the number but playlistend works only with integer so you must add `^` before the number like example above.
You can add tuple and dict also. Use double quotes inside dict.

<b>Multi links only by replying to first link</b>: -m
<code>/{cmd}</code> -m 10(number of links)

<b>Bulk Download</b>: -b
<code>/{cmd}</code> link -b
Bulk can be used by text message and by replying to text file contains links seperated by new line.
You can use it only by reply to message(text/file).
All options should be along with link!

<b>All Args:</b>
1. <code>-n</code> to rename file.
2. <code>-z</code> or <code>-zip</code> to zip files.
3. <code>-b</code> or <code>-bulk</code> to download bulk links.
4. <code>-m</code> or <code>-multi</code> to download multi links.
5. <code>-sd</code> or <code>-samedir</code> to download multi links within same upload directory.
6. <code>-s</code> or <code>-select</code> to select files from torrent.
7. <code>-index</code> to enter index link.
8. <code>-o</code> or <code>-opt</code> or <code>-options</code> to add yt-dlp options.
"""

MIRROR_HELP_MESSAGE = """
<b><u>Mirror</u></b>:
<code>/{cmd}</code> link
Or reply to the link with <code>/{cmd}</code>

<b><u>Rename</u></b>: -n
<code>/{cmd}</code> link -n new_name
Note: It doesn't work with torrents.

<b><u>Direct Link Authorization</u></b>: -u or -username and -p or -password
<code>/{cmd}</code> link -u your_username -p your_password

<b>Direct link custom headers</b>: -h
<code>/cmd</code> link -h Key: value Key1: value1

<b><u>Zip/Unzip</u></b>: -z or -zip and -e or -uz or -unzip
<code>/{cmd}</code> link -e password (extract password protected)
<code>/{cmd}</code> link -z password (zip password protected)
<code>/{cmd}</code> link -z password -e (extract and zip password protected)
<code>/{cmd}</code> link -e password -z password (extract password protected and zip password protected)
<b><u>Note</u></b>: When both extract and zip added with cmd it will extract first and then zip, so always extract first

<b><u>Multi links by replying to first link/file</u></b>: -m
<code>/{cmd}</code> -m 10(number of links/files)

<b><u>Bulk Download</u></b>: -b or -bulk
<code>/{cmd}</code> link -b
Bulk can be used by text message and by replying to text file contains links seperated by new line.
You can use it only by reply to message(text/file).
All options should be along with link!

<b><u>Join Splitted Files</u></b>: -j or -join
This option will only work before extract and zip
If your link have splitted files:
<code>/{cmd}</code> link -j

<b><u>All Arguments</u></b>:
1. -n to rename file.
2. -z or -zip to zip files.
3. -e or -uz or -unzip to extract/unzip files from zip.
4. -b or -bulk to download bulk links.
5. -m to download multi links.
6. -j or -join to join splitted files.
7. -index to enter index link.
8. -u or -username to enter username.
9. -p or -password to enter password.
"""

RSS_HELP_MESSAGE = """
<b><u>Use this format to add feed url</u></b>:
Title1 link (required)
Title2 link -c cmd -inf xx -exf xx
Title3 link -c cmd -d ratio:time -z password

-c command + any arg
-inf For included words filter.
-exf For excluded words filter.

<b><u>Example</u></b>: Title https://www.rss-url.com inf: 1080 or 720 or 144p|mkv or mp4|hevc exf: flv or web|xxx opt: up: mrcc:remote:path/subdir rcf: --buffer-size:8M|key|key:value
This filter will parse links that it's titles contains `(1080 or 720 or 144p) and (mkv or mp4) and hevc` and doesn't conyain (flv or web) and xxx` words. You can add whatever you want.

<b><u>Another example</u></b>: inf:  1080  or 720p|.web. or .webrip.|hvec or x264. This will parse titles that contains ( 1080  or 720p) and (.web. or .webrip.) and (hvec or x264). I have added space before and after 1080 to avoid wrong matching. If this `10805695` number in title it will match 1080 if added 1080 without spaces after it.

<b><u>Filter Notes</u></b>:
1. | means and.
2. Add `or` between similar keys, you can add it between qualities or between extensions, so don't add filter like this f: 1080|mp4 or 720|web because this will parse 1080 and (mp4 or 720) and web ... not (1080 and mp4) or (720 and web)."
3. You can add `or` and `|` as much as you want."
4. Take look on title if it has static special character after or before the qualities or extensions or whatever and use them in filter to avoid wrong match.
Timeout: 60 sec.
"""

CLONE_HELP_MESSAGE = """
Send Gdrive|Gdot|Filepress|Filebee|Appdrive|Gdflix link or rclone path along with command or by replying to the link/rc_path by command.

<b>Multi links only by replying to first gdlink or rclone_path:</b>
<code>/{cmd}</code> -m 10(number of links/paths)

<b>Gdrive:</b>
<code>/{cmd}</code> gdrivelink

<b>Rclone:</b>
<code>/{cmd}</code> (rcl or rclone_path) -up (rcl or rclone_path) -rcf flagkey:flagvalue|flagkey|flagkey:flagvalue

<b><u>Note</u></b>: If -up not specified then rclone destination will be the RCLONE_PATH from config.env
"""

CAT_SEL_HELP_MESSAGE = """

Reply to an active /{cmd} which was used to start the download or add gid along with {cmd}
This command mainly for change category incase you decided to change category from already added download.
But you can always use /{mir} with to select category before download start.

<b><u>Upload Custom Drive</u></b>
<code>/{cmd}</code> -id <code>drive_folder_link</code> or <code>drive_id</code> -index <code>https://anything.in/0:</code> gid or by replying to active download
drive_id must be folder id and index must be url else it will not accept.
"""

TOR_SEL_HELP_MESSAGE = """

Reply to an active <code>/{cmd}</code> which was used to start the qb-download or add gid along with cmd\n\n
This command mainly for selection incase you decided to select files from already added torrent.
But you can always use <code>/{mir}</code> with arg `-s` to select files before download start.
"""

PASSWORD_ERROR_MESSAGE = """
<b>This link requires a password!</b>
- Insert sign <b>::</b> after the link and write the password after the sign.

<b>Example:</b> {}::love you

Note: No spaces between the signs <b>::</b>
For the password, you can use a space!
"""
