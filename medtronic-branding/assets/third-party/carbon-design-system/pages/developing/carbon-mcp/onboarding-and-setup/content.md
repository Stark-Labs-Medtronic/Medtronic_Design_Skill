# Carbon MCP – Carbon Design System

Source: https://www.carbondesignsystem.com/developing/carbon-mcp/onboarding-and-setup/

# Carbon MCP

Follow these steps to configure your AI application or AI agent to use Carbon
MCP.

- [Step 1: Using your IBMid (w3id) or functional ID](https://carbondesignsystem.com/developing/carbon-mcp/onboarding-and-setup/#step-1:-using-your-ibmid-(w3id)-or-functional-id)

- [Step 2: Getting access credentials](https://carbondesignsystem.com/developing/carbon-mcp/onboarding-and-setup/#step-2:-getting-access-credentials)

- [Step 3: Connecting to IBM Bob and other MCP clients](https://carbondesignsystem.com/developing/carbon-mcp/onboarding-and-setup/#step-3:-connecting-to-ibm-bob-and-other-mcp-clients)

- [Step 4: Adding the carbon-builder skill](https://carbondesignsystem.com/developing/carbon-mcp/onboarding-and-setup/#step-4:-adding-the-carbon-builder-skill)

## Step 1: Using your IBMid (w3id) or functional ID

When going through the OAuth onboarding process, you will need to authenticate
with your IBMid (w3id for IBMers). If you need an IBMid, create one
[here](https://www.ibm.com/account/reg/us-en/signup?formid=urx-19776).

IBM product teams also have the option of authenticating via a functional ID. If
your team needs a functional ID, create one
[here](https://w3.ibm.com/#/support/article/04535/drms_addrecord?section=fid).

## Step 2: Getting access credentials

This step will launch the authorization flow to generate Carbon MCP
authentication credentials, which can be provided to your MCP client.

IBMers will be provided authentication credentials immediately upon clicking
the link below and signing in. All other users will be prompted to request
access.

### Access request workflow

1. [ Visit this link to generate your token and session ID](https://mcp.carbondesignsystem.com/mcp/auth/ibmid/web)

2. Request access if prompted

3. Check your email for the activation link

4. Copy your credentials: to add to your Carbon MCP configuration

## Step 3: Connecting to IBM Bob and other MCP clients

The IBM Cloud deployment of the Carbon MCP is available at
`https://mcp.carbondesignsystem.com/mcp`.

Here’s how to set it up in Bob and other common MCP clients:

- BobThere are **two steps** required to set up Carbon MCP in Bob. First, you need to
install **Carbon MCP** from the Bob Marketplace. Then, you need to install the[carbon-builder skill](https://carbondesignsystem.com/developing/carbon-mcp/onboarding-and-setup/#step-4:-adding-the-carbon-builder-skill).Step 1: Installing Carbon MCP
In Bob, select the settings icon in the upper right.

      
  
    

Select the **MCP** tab, then search for **“Carbon”** in the text field. Click
the **Install** button.

      
  
    

Enter your Carbon **access token** and **session ID** in the modal dialogue,
then click **Install**.
warning iconIt is not recommended to choose “Project (current workspace)” as it can
potentially introduce the risk of your token being committed to your
repository.

      
  
    

You will see a confirmation of a successful installation.

      
  
    Step 2: Installing the carbon-builder skill
Now that you’ve installed Carbon MCP, you need to install the carbon-builder
skill, which provides Carbon-specific guidance to help the model generate better
output.
Follow the instructions in _Step 4: Adding the carbon-builder skill_ to install
the[carbon-builder skill](https://carbondesignsystem.com/developing/carbon-mcp/onboarding-and-setup/#step-4:-adding-the-carbon-builder-skill)
for Bob.

- Claude Code
Use the Claude Code CLI and replace the `<TOKEN>` and `<SESSION>` with your
Carbon MCP auth credentials

claude mcp add-json carbon-mcp '{"type":"http","url":"https://mcp.carbondesignsystem.com/mcp","headers":{"Authorization":"Bearer <TOKEN>","X-MCP-Session":"<SESSION>"}}'Copy to clipboard

Verify that Claude Code recognizes Carbon MCP by running `claude mcp list`

- Claude DesktopCarbon MCP can be set up in Claude Desktop as an Extension or Custom Connector.
This section describes how to make both connections.Adding Carbon MCP as an Extension
Open Settings > Extensions > Advanced Settings


      
  
    

Click Install Extension


      
  
    

Install the `Carbon MCP Claude Desktop extension`, which can be downloaded
[here](https://carbondesignsystem.com/developing/carbon-mcp/files/carbon-mcp-claude-extension.mcpb).


      
  
    

      
  
    

Enter your Carbon MCP auth token and session ID in the modal, click Save to
confirm.


      
  
    

Verify that the Carbon MCP extension is configured by ensuring the toggle is
switched on and shows as Enabled.


      
  
    

      
  
    

Adding Carbon MCP as a Custom Connector
Open Settings > Connectors
Click on Add Custom Connector
When prompted for a name, enter `carbon-mcp`
Under the Remote MCP server URL input, use
`https://mcp.carbondesignsystem.com/mcp`
Click Add

- CursorCarbon MCP can be set up in Cursor in one of the following ways:
[](https://cursor.com/en-US/install-mcp?name=carbon-mcp&config=eyJ0eXBlIjoic3RyZWFtYWJsZS1odHRwIiwidXJsIjoiaHR0cHM6Ly9tY3AuY2FyYm9uZGVzaWduc3lzdGVtLmNvbS9tY3AiLCJkaXNhYmxlZCI6ZmFsc2UsInRpbWVvdXQiOjYwMCwiaGVhZGVycyI6eyJBdXRob3JpemF0aW9uIjoiIiwiWC1NQ1AtU2Vzc2lvbiI6IiJ9LCJhbHdheXNBbGxvdyI6WyJjb2RlX3NlYXJjaCIsImRvY3Nfc2VhcmNoIl19)


Use the “Add to Cursor” button shown above to automatically configure the MCP
server.


Alternatively, manually configure the MCP server by opening the Command
Palette and following the steps below.


      
  
    

Search for and select “View: Open MCP Settings.”


      
  
    

In the MCP Settings view, click “Add Custom MCP”.


      
  
    

It will open a file with your MCP servers where you can add the following
configuration:

{    "mcpServers": {        "carbon-mcp": {            "type": "streamable-http",            "url": "https://mcp.carbondesignsystem.com/mcp",            "disabled": false,            "timeout": 600,            "headers": {                "Authorization": "Bearer <TOKEN>",Copy to clipboardShow more

Replace `<TOKEN>` and `<SESSION>` with your actual Carbon MCP auth
credentials. Save and close the file, then restart Cursor to apply the
changes.


      
  
    

Verify that the Carbon MCP extension is configured by ensuring the toggle is
switched on and shows as Enabled.

- CodexCarbon MCP can be set up in Codex by editing your `~/.codex/config.toml`.
[mcp_servers.carbon_mcp]enabled = trueurl = "https://mcp.carbondesignsystem.com/mcp"enabled_tools = ["code_search", "docs_search", "get_charts"]
[mcp_servers.carbon_mcp.http_headers]Authorization = "Bearer <TOKEN>"X-MCP-Session = "<SESSION>"Copy to clipboard

Replace `<TOKEN>` and `<SESSION>` with your actual Carbon MCP auth
credentials. Save and close the file, then restart Codex to apply the changes.
Verify that the Carbon MCP extension is configured by ensuring the toggle is
switched on and shows as Enabled.

- Figma MakeFor IBMers:

Open Figma Make and navigate to click “Connectors”
Select the **IBM** tab
Click the **Connect** button next to Carbon MCP
A browser window will open — sign in with your IBMid when prompted
After signing in successfully, return to Figma Make. The Carbon MCP connector
dialogue should still be open (if not, reopen Connectors and select the IBM
tab)
Toggle on the **Enable write tools** button
For each of the following tools, open its dropdown and select **Always run**:

`doc_search`
`code_search`
`get_charts`


Click **Back**, then click **X** to close the Connectors menu

**Starting your first Make with Carbon MCP:**
In Figma Make, create a new Make file
Select a LLM model from the model selector. _NOTE: Gemini was observed to
consume fewer tokens, while Anthropic’s Claude Opus 4.6 model (or later)
tended to produce more accurate and complete code output_
Click **Add context** in the chat box, then select **Carbon MCP** from your
connectors to attach it to the session
Paste or attach your input design (e.g. a Figma frame or image), then include
the suggested
[user prompt](https://carbondesignsystem.com/developing/carbon-mcp/files/figma-make-user-prompt.txt) in the
same message and send it to begin generation
Once generation begins, Figma Make will create an initial draft. Before
accepting it, switch to the **Code** view (top of the Make canvas)
Open the [GUIDELINES.txt](https://carbondesignsystem.com/developing/carbon-mcp/files/GUIDELINES.txt) file,
copy its full contents, and paste them into `GUIDELINES.md` in the code view
Return to the chat and continue the conversation — the model will incorporate
these guidelines going forward
For non-IBMers:
info iconTo complete the steps below, your Figma admin must enable user creation of
custom connectors.

Open Figma Make and navigate to click “Connectors”
Select the **Created by you** tab
Click the **Create connector** button
In the Create connector dialogue, enter `carbon-mcp` as the name and click
**Next**
In the **MCP server URL** field, enter
`https://mcp.carbondesignsystem.com/mcp` and click **Create**
Click the **Connect** button next to Carbon MCP
A browser window will open — sign in with your Figma account when prompted
After signing in successfully, return to Figma Make. The Carbon MCP connector
dialogue should still be open (if not, reopen Connectors and select the
Created by you tab)
Toggle on the **Enable write tools** button
For each of the following tools, open its dropdown and select **Always run**:

`doc_search`
`code_search`
`get_charts`


Click **Back**, then click **X** to close the Connectors menu

**Starting your first Make with Carbon MCP:**
In Figma Make, create a new Make file
Select a LLM model from the model selector. _NOTE: Gemini was observed to
consume fewer tokens, while Anthropic’s Claude Opus 4.6 model (or later)
tended to produce more accurate and complete code output_
Click **Add context** in the chat box, then select **Carbon MCP** from your
connectors to attach it to the session
Paste or attach your input design (e.g. a Figma frame or image), then include
the suggested
[user prompt](https://carbondesignsystem.com/developing/carbon-mcp/files/figma-make-user-prompt.txt) in the
same message and send it to begin generation
Once generation begins, Figma Make will create an initial draft. Before
accepting it, switch to the **Code** view (top of the Make canvas)
Open the [GUIDELINES.txt](https://carbondesignsystem.com/developing/carbon-mcp/files/GUIDELINES.txt) file,
copy its full contents, and paste them into `GUIDELINES.md` in the code view
Return to the chat and continue the conversation — the model will incorporate
these guidelines going forward

- GitHub Coding Agent
Open your repository in GitHub and navigate to “Settings”.


      
  
    

In the Settings sidebar, open Copilot and select “Coding agent”.


      
  
    

Add the MCP configuration

{    "mcpServers": {        "carbon-mcp": {            "type": "http",            "url": "https://mcp.carbondesignsystem.com/mcp",            "headers": {                "Authorization": "Bearer <TOKEN>",                "X-MCP-Session": "<SESSION>"            },Copy to clipboardShow more

Replace `<TOKEN>` and `<SESSION>` with your actual Carbon MCP auth
credentials, then click “Save MCP configuration”.

- VS CodeCarbon MCP can be set up in VS Code in one of the following ways:
[](vscode:mcp/install?%7B%22name%22%3A%22carbon-mcp%22%2C%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fmcp.carbondesignsystem.com%2Fmcp%22%2C%22headers%22%3A%7B%22Authorization%22%3A%22Bearer%20%24%7Binput%3Atoken%7D%22%2C%22X-MCP-Session%22%3A%22%24%7Binput%3Asession%7D%22%7D%2C%22inputs%22%3A%5B%7B%22id%22%3A%22token%22%2C%22type%22%3A%22promptString%22%2C%22description%22%3A%22Carbon%20MCP%20Token%22%2C%22password%22%3Atrue%7D%2C%7B%22id%22%3A%22session%22%2C%22type%22%3A%22promptString%22%2C%22description%22%3A%22Carbon%20MCP%20Session%20ID%22%7D%5D%7D)


Use the “Install carbon-mcp” button shown above to automatically configure the
MCP server.


Alternatively, manually use VS Code CLI and replace the `<TOKEN>` and
`<SESSION>` with your Carbon MCP auth credentials

code --add-mcp '{"name":"carbon-mcp","type":"http","url":"https://mcp.carbondesignsystem.com/mcp","headers":{"Authorization":"Bearer <TOKEN>","X-MCP-Session":"<SESSION>"}}'Copy to clipboard

- Other clientsIf the MCP client you are using is not listed, refer to their documentation for
`remote servers` and use `https://mcp.carbondesignsystem.com/mcp` as the URL.

Additionally, an `llms.txt` file is available [here](https://carbondesignsystem.com/llms.txt) — a structured
index of Carbon Design System documentation, components, and source repositories
for AI tools and LLMs.

## Step 4: Adding the carbon-builder skill

For best results with Carbon MCP, install the
[carbon-builder skill](https://carbondesignsystem.com/developing/carbon-mcp/files/carbon-builder.zip). The
skill provides Carbon-specific context that guides AI agents to follow Carbon
conventions, use the right components, and produce consistent output.

Follow the instructions for the clients below.

- Bob
Select the Bob `Advanced` mode, which is required to support skills.
Download the
[carbon-builder skill](https://carbondesignsystem.com/developing/carbon-mcp/files/carbon-builder.zip) and
unzip it.
Place the skill in `.bob/skills/` at your project root (project-scoped) or in
`~/.bob/skills/` (global).

Bob reads `name` and `description` from `SKILL.md` to determine when to activate
the skill. The `references/` files are automatically available to Bob once the
skill is active. Verify the skill is visible by running `/list-skills` inside
Bob.
**Project-scoped (recommended for teams):**
mkdir -p /path/to/your-project/.bob/skillscp -r carbon-builder /path/to/your-project/.bob/skills/Copy to clipboard

Commit `.bob/skills/carbon-builder/` to your repository so the skill is shared
across the team without each developer needing to install it separately.

**Global (available in all projects on this machine):**
mkdir -p ~/.bob/skillscp -r carbon-builder ~/.bob/skills/Copy to clipboard

- Claude CodeClaude Code discovers skills automatically from `.claude/skills/` at your
project root. No additional configuration is needed beyond having carbon-mcp
configured as an MCP server.

Download the
[carbon-builder skill](https://carbondesignsystem.com/developing/carbon-mcp/files/carbon-builder.zip) and
unzip it.

**Project-scoped (recommended for teams):**
# From the directory where you unzipped the downloadmkdir -p /path/to/your-project/.claude/skillscp -r carbon-builder /path/to/your-project/.claude/skills/Copy to clipboard

Commit `.claude/skills/carbon-builder/` to your repository so the skill is
version-tracked alongside the project and available to every developer on the
team without a separate install.

**Global (available in all projects on this machine):**
mkdir -p ~/.claude/skillscp -r carbon-builder ~/.claude/skills/Copy to clipboard

- Claude DesktopDownload the
[carbon-builder skill](https://carbondesignsystem.com/developing/carbon-mcp/files/carbon-builder.zip). No need
to unzip; Claude Desktop accepts the ZIP file directly.

Open **Settings > Capabilities** and ensure **Cloud code execution and file
creation** is enabled
Navigate to **Customize > Skills**
Click the `+` to **Upload a skill** and select the downloaded
`carbon-builder.zip`

Claude Desktop will activate the skill automatically based on its description.
You can verify it appears in your Skills list and toggle it on or off from
there.
info iconCustom skills are private to your account. Each team member will need to
upload the skill individually.

- CursorCursor uses MDC-format rule files in `.cursor/rules/`.


Download the
[carbon-builder skill](https://carbondesignsystem.com/developing/carbon-mcp/files/carbon-builder.zip) and
unzip it.


Create the rules directory:


mkdir -p .cursor/rulesCopy to clipboard

Create `.cursor/rules/carbon-builder.mdc`:

---description:  Carbon Design System expert — activate for Carbon components, Charts, IBM  Products, AI Chat, and iconsalwaysApply: false---
[paste the body of SKILL.md here — everything below the closing --- of thefrontmatter] [paste any reference file content from the references/ directoryCopy to clipboardShow more
info iconCursor does not auto-load the `references/` directory. Inline the
content of any reference files you need directly into the MDC file, or
create additional `.mdc` rule files with 
`alwaysApply: false`.
Ensure carbon-mcp is configured as an MCP server in Cursor’s settings.

- GitHub Coding AgentGitHub Copilot coding agent supports Agent Skills from your repository in
`.github/skills/`. Unlike local desktop clients, there is no global install
location because the agent runs against the contents of the repository.

Download the
[carbon-builder skill](https://carbondesignsystem.com/developing/carbon-mcp/files/carbon-builder.zip) and
unzip it.

**Repository-scoped install:**
mkdir -p /path/to/your-project/.github/skillscp -r carbon-builder /path/to/your-project/.github/skills/Copy to clipboard
Commit `.github/skills/carbon-builder/` to your repository so the skill is
available to GitHub Copilot coding agent when it works on issues, pull requests,
or delegated coding tasks for that repo.
GitHub Copilot coding agent reads the `name` and `description` fields from
`SKILL.md` and loads the skill automatically when the current task matches the
skill’s purpose.

- VS Code
VS Code supports Agent Skills as project skills in `.github/skills/`,
`.claude/skills/`, or `.agents/skills/`, and as personal skills in
`~/.copilot/skills/`, `~/.claude/skills/`, or `~/.agents/skills/`.


Use `.github/skills/` in your repository if you want the skill to be shared
with your team. Use `~/.copilot/skills/` if you want it available across all
of your local projects in VS Code.


Download the
[carbon-builder skill](https://carbondesignsystem.com/developing/carbon-mcp/files/carbon-builder.zip) and
unzip it.

**Project-scoped (recommended for teams):**
mkdir -p /path/to/your-project/.github/skillscp -r carbon-builder /path/to/your-project/.github/skills/Copy to clipboard

Commit `.github/skills/carbon-builder/` to your repository so the skill is
version-tracked and available to other developers using VS Code on the same
repo.

**Global (available in all projects on this machine):**
mkdir -p ~/.copilot/skillscp -r carbon-builder ~/.copilot/skills/Copy to clipboard
To verify the skill is available in VS Code:
Open the Command Palette and run **Chat: Open Chat Customizations**
Open the **Skills** tab and confirm `carbon-builder` appears in the list
Or type `/skills` in chat to open the skills menu

VS Code reads the `name` and `description` from `SKILL.md` and loads the skill
automatically when it is relevant to the current task.

- Other clientsIf your MCP client is not listed above, refer to its documentation for
installing skills.
Most agent tools that support custom instructions load context from a Markdown
file or a dedicated directory at the project root. Common patterns include:


A single instructions file such as `AGENTS.md`, `AGENT.md`, or
`.agent/instructions.md`


A rules or skills directory such as `.agent/skills/`, `.rules/`, or a
client-specific equivalent


Download the
[carbon-builder skill](https://carbondesignsystem.com/developing/carbon-mcp/files/carbon-builder.zip) and
unzip it.


To install the carbon-builder skill in any of these clients, paste the body of
`SKILL.md` (everything below the closing `---` of the frontmatter) into the
appropriate file. If the client supports a directory of files, copy the
`carbon-builder/` folder there. Refer to your client’s documentation for the
exact path and format it expects.

## Code samples

```
claude mcp add-json carbon-mcp '{"type":"http","url":"https://mcp.carbondesignsystem.com/mcp","headers":{"Authorization":"Bearer <TOKEN>","X-MCP-Session":"<SESSION>"}}'Copy to clipboard
```

```bash
claude mcp add-json carbon-mcp '{"type":"http","url":"https://mcp.carbondesignsystem.com/mcp","headers":{"Authorization":"Bearer <TOKEN>","X-MCP-Session":"<SESSION>"}}'
```

```
{    "mcpServers": {        "carbon-mcp": {            "type": "streamable-http",            "url": "https://mcp.carbondesignsystem.com/mcp",            "disabled": false,            "timeout": 600,            "headers": {                "Authorization": "Bearer <TOKEN>",Copy to clipboardShow more
```

```markdown
{    "mcpServers": {        "carbon-mcp": {            "type": "streamable-http",            "url": "https://mcp.carbondesignsystem.com/mcp",            "disabled": false,            "timeout": 600,            "headers": {                "Authorization": "Bearer <TOKEN>",
```

```
[mcp_servers.carbon_mcp]enabled = trueurl = "https://mcp.carbondesignsystem.com/mcp"enabled_tools = ["code_search", "docs_search", "get_charts"]
[mcp_servers.carbon_mcp.http_headers]Authorization = "Bearer <TOKEN>"X-MCP-Session = "<SESSION>"Copy to clipboard
```

```markdown
[mcp_servers.carbon_mcp]enabled = trueurl = "https://mcp.carbondesignsystem.com/mcp"enabled_tools = ["code_search", "docs_search", "get_charts"]
[mcp_servers.carbon_mcp.http_headers]Authorization = "Bearer <TOKEN>"X-MCP-Session = "<SESSION>"
```

```
{    "mcpServers": {        "carbon-mcp": {            "type": "http",            "url": "https://mcp.carbondesignsystem.com/mcp",            "headers": {                "Authorization": "Bearer <TOKEN>",                "X-MCP-Session": "<SESSION>"            },Copy to clipboardShow more
```

```markdown
{    "mcpServers": {        "carbon-mcp": {            "type": "http",            "url": "https://mcp.carbondesignsystem.com/mcp",            "headers": {                "Authorization": "Bearer <TOKEN>",                "X-MCP-Session": "<SESSION>"            },
```

```
code --add-mcp '{"name":"carbon-mcp","type":"http","url":"https://mcp.carbondesignsystem.com/mcp","headers":{"Authorization":"Bearer <TOKEN>","X-MCP-Session":"<SESSION>"}}'Copy to clipboard
```

```bash
code --add-mcp '{"name":"carbon-mcp","type":"http","url":"https://mcp.carbondesignsystem.com/mcp","headers":{"Authorization":"Bearer <TOKEN>","X-MCP-Session":"<SESSION>"}}'
```

```
mkdir -p /path/to/your-project/.bob/skillscp -r carbon-builder /path/to/your-project/.bob/skills/Copy to clipboard
```

```bash
mkdir -p /path/to/your-project/.bob/skillscp -r carbon-builder /path/to/your-project/.bob/skills/
```

```
mkdir -p ~/.bob/skillscp -r carbon-builder ~/.bob/skills/Copy to clipboard
```

```bash
mkdir -p ~/.bob/skillscp -r carbon-builder ~/.bob/skills/
```

```
# From the directory where you unzipped the downloadmkdir -p /path/to/your-project/.claude/skillscp -r carbon-builder /path/to/your-project/.claude/skills/Copy to clipboard
```

```bash
# From the directory where you unzipped the downloadmkdir -p /path/to/your-project/.claude/skillscp -r carbon-builder /path/to/your-project/.claude/skills/
```

```
mkdir -p ~/.claude/skillscp -r carbon-builder ~/.claude/skills/Copy to clipboard
```

```bash
mkdir -p ~/.claude/skillscp -r carbon-builder ~/.claude/skills/
```

```
mkdir -p .cursor/rulesCopy to clipboard
```

```bash
mkdir -p .cursor/rules
```

```
---description:  Carbon Design System expert — activate for Carbon components, Charts, IBM  Products, AI Chat, and iconsalwaysApply: false---
[paste the body of SKILL.md here — everything below the closing --- of thefrontmatter] [paste any reference file content from the references/ directoryCopy to clipboardShow more
```

```markdown
---description:  Carbon Design System expert — activate for Carbon components, Charts, IBM  Products, AI Chat, and iconsalwaysApply: false---
[paste the body of SKILL.md here — everything below the closing --- of thefrontmatter] [paste any reference file content from the references/ directory
```

```
mkdir -p /path/to/your-project/.github/skillscp -r carbon-builder /path/to/your-project/.github/skills/Copy to clipboard
```

```bash
mkdir -p /path/to/your-project/.github/skillscp -r carbon-builder /path/to/your-project/.github/skills/
```

```
mkdir -p /path/to/your-project/.github/skillscp -r carbon-builder /path/to/your-project/.github/skills/Copy to clipboard
```

```bash
mkdir -p /path/to/your-project/.github/skillscp -r carbon-builder /path/to/your-project/.github/skills/
```

```
mkdir -p ~/.copilot/skillscp -r carbon-builder ~/.copilot/skills/Copy to clipboard
```

```bash
mkdir -p ~/.copilot/skillscp -r carbon-builder ~/.copilot/skills/
```
