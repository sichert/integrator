declare namespace RT {
  type Ably = {
    apiKye: string
  }

  type Abstractapi = {
    apiKey: string
  }

  type Accelo = {
    clientId: string,
    deployment: string,
    clientSecret: string
  }

  type Actimo = {
    apiKey: string
  }

  type Acumbamail = {
    authToken: string
  }

  type Adhook = {
    token: string
  }

  type Adrapid = {
    apiToken: string
  }

  type AeroWorkflow = {
    apiKey: string
  }

  type Ai21 = {
    apiKey: string
  }

  type Airtable = {
    apiKey: string
  }

  type AirtableTable = {
    baseId: string,
    tableName: string
  }

  type AnsibleInventory = {
    content: string
  }

  type Anthropic = {
    apiKey: string
  }

  type Apify = {
    token: string
  }

  type ApifyApiKey = {
    api_key: string
  }

  type ApifyWebhookConfig = {
    url: string,
    token: string
  }

  type ApiKeyAuth = {
    api_key_header: string,
    api_key_secret: string
  }

  type Apollo = {
    apiKey: string
  }

  type Appwrite = {
    key: string,
    project: string,
    endpoint: string,
    self_signed: boolean
  }

  type ArcgisAccount = {
    password: string,
    username: string
  }

  type Asana = {
    token: string
  }

  type Assemblyai = {
    apiKey: string
  }

  type Attio = {
    token: string
  }

  type Aws = {
    region: string,
    awsAccessKeyId: string,
    awsSecretAccessKey: string
  }

  type AwsBedrock = {
    apiKey: string,
    region: string,
    awsAccessKeyId: string,
    awsSecretAccessKey: string
  }

  type AwsOidc = {
    region: string,
    roleArn: string
  }

  type Azure = {
    azureClientId: string,
    azureTenantId: string,
    azureClientSecret: string
  }

  type AzureBlob = {
    useSSL: boolean,
    endpoint: string,
    accessKey: string,
    accountName: string,
    containerName: string
  }

  type AzureOauth = {
    token: string
  }

  type AzureOpenai = {
    apiKey: string,
    baseUrl: string
  }

  type AzureWorkloadIdentity = {
    useSSL: boolean,
    accountName: string,
    containerName: string
  }

  type BambooHr = {
    apiKey: string,
    companyDomain: string
  }

  type Baremetrics = {
    apiKey: string
  }

  type Baserow = {
    token: string,
    base_url: string
  }

  type BaserowTable = {
    table_id: number,
    database_id: number
  }

  type BasicHttpAuth = {
    password: string,
    username: string
  }

  type BasisTheory = {
    apiKey: string
  }

  type Beamer = {
    apiKey: string
  }

  type Bigquery = {
    type: string,
    auth_uri: string,
    client_id: string,
    token_uri: string,
    project_id: string,
    private_key: string,
    client_email: string,
    private_key_id: string,
    client_x509_cert_url: string,
    auth_provider_x509_cert_url: string
  }

  type Bitbucket = {
    password: string,
    username: string
  }

  type Bitly = {
    token: string
  }

  type Bluesky = {
    password: string,
    username: string
  }

  type Botify = {
    token: string
  }

  type Box = {
    token: string
  }

  type Brevo = {
    apiKey: string
  }

  type Brex = {
    token: string
  }

  type Buttondown = {
    token: string
  }

  type Cacertificate = {
    certificate: string
  }

  type Calendly = {
    token: string
  }

  type Campayn = {
    apiKey: string
  }

  type Certopus = {
    apiKey: string
  }

  type Chromadb = {
    ssl: boolean,
    host: string,
    port: number,
    tenant: string,
    database: string
  }

  type Circleci = {
    token: string
  }

  type Clerk = {
    apiKey: string
  }

  type Clickhouse = {
    host: string,
    password: string,
    username: string
  }

  type Clickup = {
    token: string
  }

  type Cloudflare = {
    key: string,
    email: string,
    token: string
  }

  type Cockroachdb = {
    token: string
  }

  type Codat = {
    encodedKey: string
  }

  type Cohere = {
    apiKey: string
  }

  type ComapeoServer = {
    server_url: string,
    access_token: string
  }

  type Confluence = {
    email: string,
    baseUrl: string,
    apiToken: string
  }

  type Contentful = {
    spaceId: string,
    accessToken: string,
    environment: string
  }

  type Contiguity = {
    token: string
  }

  type Convertkit = {
    apiSecret: string
  }

  type Currencyapi = {
    apiKey: string
  }

  type Customai = {
    api_key: string,
    base_url: string
  }

  type Datadog = {
    apiKey: string,
    appKey: string,
    apiBase: string
  }

  type Datocms = {
    apiKey: string
  }

  type Deel = {
    apiKey: string
  }

  type DeepInfra = {
    token: string
  }

  type Deepl = {
    apiKey: string,
    baseUrl: string
  }

  type Deepseek = {
    api_key: string
  }

  type Digitalocean = {
    token: string
  }

  type DiscordBotConfiguration = {
    public_key: string,
    application_id: string
  }

  type DiscordWebhook = {
    webhook_url: string
  }

  type Discourse = {
    apiKey: string,
    apiUsername: string,
    defaultHost: string
  }

  type Docspring = {
    tokenId: string,
    tokenSecret: string
  }

  type Dust = {
    apiKey: string,
    workspaceId: string
  }

  type Dynatrace = {
    accessToken: string,
    environmentId: string,
    environmentUrl: string
  }

  type Edgedb = {
    dsn: string,
    host: string,
    port: number,
    user: string,
    database: string,
    password: string,
    secretKey: string,
    instanceName: string
  }

  type Enode = {
    token: string
  }

  type Exa = {
    apiKey: string
  }

  type Faunadb = {
    region: string,
    secret: string
  }

  type Figma = {
    token: string
  }

  type Firebase = {
    appId: string,
    apiKey: string,
    projectId: string,
    authDomain: string,
    measurementId: string,
    storageBucket: string,
    messagingSenderId: string
  }

  type Fly = {
    token: string
  }

  type Formstack = {
    token: string
  }

  type Foxentry = {
    apiKey: string
  }

  type Freshdesk = {
    apiKey: string,
    baseUrl: string
  }

  type Funkwhale = {
    token: string,
    baseUrl: string
  }

  type Gcal = {
    token: string
  }

  type Gcloud = {
    type: string,
    auth_uri: string,
    client_id: string,
    token_uri: string,
    project_id: string,
    private_key: string,
    client_email: string,
    private_key_id: string,
    client_x509_cert_url: string,
    auth_provider_x509_cert_url: string
  }

  type GcloudStorage = {
    bucket: string,
    serviceAccountKey: any
  }

  type GcpServiceAccount = {
    type: string,
    auth_uri: string,
    client_id: string,
    token_uri: string,
    project_id: string,
    private_key: string,
    client_email: string,
    private_key_id: string,
    client_x509_cert_url: string,
    auth_provider_x509_cert_url: string
  }

  type Gdocs = {
    token: string
  }

  type Gdrive = {
    token: string
  }

  type Gforms = {
    token: string
  }

  type Gfw = {
    api_key: string
  }

  type Ghostcms = {
    apiKey: string,
    apiUrl: string
  }

  type Gitbook = {
    token: string
  }

  type Github = {
    token: string
  }

  type Gitlab = {
    token: string,
    baseUrl: string
  }

  type GitRepository = {
    url: string,
    branch: string,
    folder: string,
    gpg_key: any,
    is_github_app: boolean
  }

  type Gmail = {
    token: string
  }

  type Googleai = {
    api_key: string
  }

  type Gorgias = {
    apiKey: string,
    domain: string,
    username: string
  }

  type GpgKey = {
    email: string,
    passphrase: string,
    private_key: string
  }

  type Graphql = {
    base_url: string,
    bearer_token: string,
    custom_headers: any
  }

  type Greip = {
    apiKey: string
  }

  type Grist = {
    host: string,
    apiKey: string
  }

  type Groq = {
    api_key: string
  }

  type Groqai = {
    api_key: string
  }

  type Gsheets = {
    token: string
  }

  type Gworkspace = {
    token: string
  }

  type Holded = {
    apiKey: string
  }

  type Hubspot = {
    token: string
  }

  type IfsCloudOidc = {
    server: string,
    clientId: string,
    oidcPath: string,
    clientSecret: string
  }

  type Intercom = {
    token: string,
    apiVersion: string
  }

  type Ipinfo = {
    token: string
  }

  type Jira = {
    domain: string,
    password: string,
    username: string
  }

  type Jotform = {
    apiKey: string,
    baseUrl: string
  }

  type JsonSchema = {
    schema: any
  }

  type Kafka = {
    brokers: string[],
    security: any
  }

  type Klaviyo = {
    apiKey: string
  }

  type Kobotoolbox = {
    api_key: string,
    server_url: string
  }

  type Kustomer = {
    apiKey: string
  }

  type Langfuse = {
    base_url: string,
    public_key: string,
    secret_key: string
  }

  type Ldap = {
    server: string,
    use_ssl: boolean,
    bind_user: string,
    ssl_validate: boolean,
    bind_password: string
  }

  type Leonardoai = {
    apiKey: string
  }

  type Linear = {
    apiKey: string
  }

  type Linkding = {
    token: string,
    baseUrl: string
  }

  type Linkedin = {
    token: string
  }

  type Linode = {
    token: string
  }

  type Lumaai = {
    apiKey: string
  }

  type Magento = {
    accessToken: string,
    consumerKey: string,
    consumerSecret: string,
    accessTokenSecret: string
  }

  type Mailchimp = {
    server: string,
    api_key: string
  }

  type Mailerlite = {
    apiToken: string
  }

  type Mailgun = {
    api_key: string
  }

  type Mastodon = {
    token: string,
    baseUrl: string
  }

  type Matrix = {
    token: string,
    baseUrl: string
  }

  type Mcp = {
    url: string,
    name: string,
    token: string,
    headers: any
  }

  type Meteosource = {
    tier: string,
    apiKey: string
  }

  type Mezmo = {
    apiKey: string
  }

  type Miro = {
    token: string
  }

  type Mistral = {
    apiKey: string
  }

  type Mollie = {
    token: string
  }

  type Mongodb = {
    db: string,
    tls: boolean,
    servers: any,
    credential: any
  }

  type MongodbRest = {
    api_key: string,
    endpoint: string
  }

  type Motimate = {
    token: string
  }

  type Mqtt = {
    tls: {
    enabled: boolean,
    ca_certificate: string,
    pkcs12_client_certificate: string,
    pkcs12_certificate_password: string
  },
    port: number,
    broker: string,
    credentials: {
    password: string,
    username: string
  }
  }

  type MsSqlServer = {
    host: string,
    port: number,
    user: string,
    dbname: string,
    ca_cert: string,
    encrypt: boolean,
    password: string,
    aad_token: any,
    trust_cert: boolean,
    instance_name: string
  }

  type MsTeamsWebhook = {
    webhook_url: string
  }

  type Mysql = {
    ssl: boolean,
    host: string,
    port: number,
    user: string,
    database: string,
    password: string,
    root_certificate_pem: string
  }

  type Nats = {
    auth: any,
    servers: string[],
    require_tls: boolean
  }

  type Neondb = {
    apiKey: string
  }

  type Netbox = {
    url: string,
    token: string
  }

  type Netlify = {
    token: string
  }

  type Newsapi = {
    apiKey: string
  }

  type Nextcloud = {
    baseUrl: string,
    password: string,
    username: string
  }

  type Nocodb = {
    table: string,
    apiUrl: string,
    xc_token: string,
    workspace: string
  }

  type Notion = {
    token: string
  }

  type Odk = {
    base_url: string,
    password: string,
    username: string,
    default_project_id: number
  }

  type Openai = {
    api_key: string,
    organization_id: string
  }

  type Openrouter = {
    api_key: string
  }

  type Oracledb = {
    user: string,
    database: string,
    password: string
  }

  type Pandadoc = {
    apiKey: string
  }

  type Paychex = {
    client_id: string,
    client_secret: string
  }

  type Paylocity = {
    token: string
  }

  type Paypal = {
    clientId: string,
    clientSecret: string
  }

  type Persona = {
    apiKey: string
  }

  type Personio = {
    clientId: string,
    clientSecret: string
  }

  type Phrase = {
    token: string,
    baseUrl: string
  }

  type Pinecone = {
    apiKey: string,
    environment: string
  }

  type Pinterest = {
    token: string
  }

  type Pipedrive = {
    apiToken: string
  }

  type Planetscale = {
    serviceToken: string,
    serviceTokenId: string
  }

  type Postgresql = {
    host: string,
    port: number,
    user: string,
    dbname: string,
    sslmode: string,
    password: string,
    root_certificate_pem: string
  }

  type Pushover = {
    user: string,
    token: string
  }

  type Qovery = {
    apiKey: string
  }

  type Quickbooks = {
    token: string,
    realmId: string,
    isSandBox: boolean
  }

  type Readme = {
    apiKey: string
  }

  type Recraft = {
    apiKey: string
  }

  type Reddit = {
    clientId: string,
    password: string,
    username: string,
    userAgent: string,
    clientSecret: string
  }

  type Render = {
    apiKey: string
  }

  type Replicate = {
    token: string
  }

  type Resend = {
    token: string
  }

  type Rss = {
    url: string
  }

  type S3 = {
    port: number,
    bucket: string,
    region: string,
    useSSL: boolean,
    endPoint: string,
    accessKey: string,
    pathStyle: boolean,
    secretKey: string
  }

  type S3AwsOidc = {
    bucket: string,
    region: string,
    roleArn: string
  }

  type SageIntacct = {
    token: string
  }

  type Salesflare = {
    apiKey: string
  }

  type Segment = {
    token: string,
    baseUrl: string
  }

  type Sendgrid = {
    token: string
  }

  type Sensortower = {
    base_url: string,
    auth_token: string
  }

  type Sentry = {
    token: string,
    region: string,
    organizationSlug: string
  }

  type Shopify = {
    token: string,
    store_name: string
  }

  type Shutterstock = {
    token: string
  }

  type SignatureAuth = {
    secret_key: string,
    signature_provider: string,
    authentication_config: {
    encoding: string,
    algorithm: string,
    signature_prefix: string,
    signature_header_name: string
  }
  }

  type Signoz = {
    apiKey: string,
    baseUrl: string
  }

  type Slack = {
    token: string
  }

  type Smartsheet = {
    token: string,
    baseUrl: string
  }

  type Smtp = {
    host: string,
    port: number,
    user: string,
    password: string
  }

  type Snowflake = {
    role: string,
    schema: string,
    database: string,
    username: string,
    warehouse: string,
    public_key: string,
    private_key: string,
    account_identifier: string
  }

  type Speechify = {
    token: string
  }

  type Spotify = {
    token: string
  }

  type Square = {
    token: string
  }

  type Stripe = {
    token: string
  }

  type Supabase = {
    key: string,
    url: string
  }

  type Surrealdb = {
    url: string,
    token: string
  }

  type Taskade = {
    token: string
  }

  type Telegram = {
    token: string
  }

  type Telnyx = {
    apiKey: string
  }

  type Terra = {
    devId: string,
    apiKey: string
  }

  type TheirStack = {
    apiKey: string
  }

  type Todoist = {
    token: string
  }

  type Togetherai = {
    api_key: string
  }

  type Toggl = {
    token: string
  }

  type Tomorrow = {
    apiKey: string
  }

  type Trello = {
    key: string,
    token: string
  }

  type Tripadvisor = {
    apiKey: string
  }

  type Turso = {
    apiToken: string
  }

  type Twilio = {
    token: string,
    accountSid: string
  }

  type TwilioMessageTemplate = {
    auth_token: string,
    recipients: string[],
    account_sid: string,
    content_sid: string,
    origin_number: string,
    message_service_sid: string
  }

  type Typeform = {
    token: string,
    baseUrl: string
  }

  type Ultravox = {
    apiKey: string
  }

  type Vectara = {
    apiKey: string
  }

  type Vercel = {
    token: string
  }

  type Visma = {
    token: string
  }

  type Weatherapi = {
    apiKey: string
  }

  type Webflow = {
    token: string
  }

  type Webscrapingai = {
    apiKey: string
  }

  type Woocommerce = {
    url: string,
    version: string,
    consumerKey: string,
    consumerSecret: string,
    queryStringAuth: boolean
  }

  type Xata = {
    apiKey: string
  }

  type Xero = {
    token: string
  }

  type Yelp = {
    apiKey: string
  }

  type Ynab = {
    token: string
  }

  type Zendesk = {
    password: string,
    username: string,
    subdomain: string
  }

  type Zixflow = {
    apiKey: string
  }

  type Zoho = {
    token: string
  }

  type Zoom = {
    accountId: string,
    oauthClientId: string,
    oauthClientSecret: string,
    webhookSecretToken: string
  }

  type Zuplo = {
    apiKey: string
  }
}