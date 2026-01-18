import json
import cloudscraper

URL = "	https://medium.com/_/graphql"

userAgent = "Your user agent"
xsrf_token = "Your Token copied from website"
uid = "Your uid"
sid = "Your sid"
Cookie = "Your Cookie string copied from website"

headers = {
    "User-Agent": userAgent,
    "Accept":"*/*",
    "Accept-Encoding":"gzip, deflate, br, zstd",
    "Accept-Language":"uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7",
    "graphql-operation":"WebInlineRecommendedFeedQuery",
    "medium-frontend-app":"lite/main-20260116-161017-b2412ec54c",
    "medium-frontend-path":"/",
    "medium-frontend-route":"homepage",
    "Cookie": Cookie,
    "content-type":"application/json",
    "Priority": "u=4",
    "x-xsrf-token": xsrf_token,
    "Referer": "https://medium.com/",
    "Origin": "https://medium.com"
}

scraper = cloudscraper.create_scraper(
    browser={
        "browser": "firefox",
        "platform": "windows",
        "desktop": True,
    }
)

payload = [
    {
        "operationName": "WebInlineRecommendedFeedQuery",
        "query": "query WebInlineRecommendedFeedQuery($paging: PagingOptions, $forceRank: Boolean) {  webRecommendedFeed(paging: $paging, forceRank: $forceRank) {    items {      ...InlineFeed_homeFeedItem      reasonString      __typename    }    pagingInfo {      next {        limit        to        source        __typename      }      __typename    }    __typename  }}fragment userUrl_user on User {  __typename  id  customDomainState {    live {      domain      __typename    }    __typename  }  hasSubdomain  username}fragment PostPreviewReason_user on User {  name  ...userUrl_user  __typename  id}fragment PostPreviewReason_tag on Tag {  normalizedTagSlug  id  displayTitle  __typename}fragment PostPreviewReason_postProviderExplanation on PostProviderExplanation {  reason  interactedUsers {    ...PostPreviewReason_user    __typename  }  tagObject {    ...PostPreviewReason_tag    __typename    id  }  __typename}fragment StreamPostPreview_postProviderExplanation on PostProviderExplanation {  ...PostPreviewReason_postProviderExplanation  __typename}fragment StreamPostPreviewImage_imageMetadata on ImageMetadata {  id  focusPercentX  focusPercentY  alt  __typename}fragment StreamPostPreviewImage_post on Post {  title  previewImage {    ...StreamPostPreviewImage_imageMetadata    __typename    id  }  __typename  id}fragment SignInOptions_user on User {  id  name  imageId  __typename}fragment SignUpOptions_user on User {  id  name  imageId  __typename}fragment SusiModal_user on User {  ...SignInOptions_user  ...SignUpOptions_user  __typename  id}fragment SusiClickable_user on User {  ...SusiModal_user  __typename  id}fragment SusiModal_post on Post {  id  creator {    id    __typename  }  __typename}fragment SusiClickable_post on Post {  id  mediumUrl  ...SusiModal_post  __typename}fragment MultiVoteCount_post on Post {  id  __typename}fragment MultiVote_post on Post {  id  creator {    id    ...SusiClickable_user    __typename  }  isPublished  ...SusiClickable_post  collection {    id    slug    __typename  }  isLimitedState  ...MultiVoteCount_post  __typename}fragment PostPreviewFooterSocial_post on Post {  id  ...MultiVote_post  allowResponses  isPublished  isLimitedState  postResponses {    count    __typename  }  __typename}fragment AddToCatalogBase_post on Post {  id  isPublished  ...SusiClickable_post  __typename}fragment AddToCatalogBookmarkButton_post on Post {  ...AddToCatalogBase_post  __typename  id}fragment BookmarkButton_post on Post {  visibility  ...SusiClickable_post  ...AddToCatalogBookmarkButton_post  __typename  id}fragment useNewsletterV3Subscription_newsletterV3 on NewsletterV3 {  id  type  slug  name  collection {    slug    __typename    id  }  user {    id    name    username    newsletterV3 {      id      __typename    }    __typename  }  __typename}fragment useNewsletterV3Subscription_user on User {  id  username  newsletterV3 {    ...useNewsletterV3Subscription_newsletterV3    __typename    id  }  __typename}fragment useAuthorFollowSubscribeButton_user on User {  id  name  ...useNewsletterV3Subscription_user  __typename}fragment useAuthorFollowSubscribeButton_newsletterV3 on NewsletterV3 {  id  name  ...useNewsletterV3Subscription_newsletterV3  __typename}fragment AuthorFollowSubscribeButton_user on User {  id  name  imageId  ...SusiModal_user  ...useAuthorFollowSubscribeButton_user  newsletterV3 {    id    ...useAuthorFollowSubscribeButton_newsletterV3    __typename  }  __typename}fragment FollowMenuOptions_user on User {  id  ...AuthorFollowSubscribeButton_user  __typename}fragment SignInOptions_collection on Collection {  id  name  __typename}fragment SignUpOptions_collection on Collection {  id  name  __typename}fragment SusiModal_collection on Collection {  name  ...SignInOptions_collection  ...SignUpOptions_collection  __typename  id}fragment PublicationFollowButton_collection on Collection {  id  slug  name  ...SusiModal_collection  __typename}fragment FollowMenuOptions_collection on Collection {  id  ...PublicationFollowButton_collection  __typename}fragment ClapMutation_post on Post {  __typename  id  clapCount  ...MultiVoteCount_post}fragment OverflowMenuItemUndoClaps_post on Post {  id  clapCount  ...ClapMutation_post  __typename}fragment NegativeSignalModal_publisher on Publisher {  __typename  id  name}fragment NegativeSignalModal_post on Post {  id  creator {    ...NegativeSignalModal_publisher    viewerEdge {      id      isMuting      __typename    }    __typename    id  }  collection {    ...NegativeSignalModal_publisher    viewerEdge {      id      isMuting      __typename    }    __typename    id  }  __typename}fragment ExplicitSignalMenuOptions_post on Post {  ...NegativeSignalModal_post  __typename  id}fragment OverflowMenu_post on Post {  id  creator {    id    ...FollowMenuOptions_user    __typename  }  collection {    id    ...FollowMenuOptions_collection    __typename  }  ...OverflowMenuItemUndoClaps_post  ...AddToCatalogBase_post  ...ExplicitSignalMenuOptions_post  __typename}fragment OverflowMenuButton_post on Post {  id  visibility  ...OverflowMenu_post  __typename}fragment PostPreviewFooterMenu_post on Post {  id  ...BookmarkButton_post  ...OverflowMenuButton_post  __typename}fragment usePostPublishedAt_post on Post {  firstPublishedAt  latestPublishedAt  pinnedAt  __typename  id}fragment Star_post on Post {  id  __typename}fragment PostPreviewFooterMeta_post on Post {  isLocked  postResponses {    count    __typename  }  ...usePostPublishedAt_post  ...Star_post  __typename  id}fragment PostPreviewFooter_post on Post {  ...PostPreviewFooterSocial_post  ...PostPreviewFooterMenu_post  ...PostPreviewFooterMeta_post  __typename  id}fragment UserAvatar_user on User {  __typename  id  imageId  membership {    tier    __typename    id  }  name  username  ...userUrl_user}fragment PostPreviewBylineAuthorAvatar_user on User {  ...UserAvatar_user  __typename  id}fragment isUserVerifiedBookAuthor_user on User {  verifications {    isBookAuthor    __typename  }  __typename  id}fragment UserLink_user on User {  ...userUrl_user  __typename  id}fragment UserName_user on User {  id  name  ...isUserVerifiedBookAuthor_user  ...UserLink_user  __typename}fragment PostPreviewByLineAuthor_user on User {  ...PostPreviewBylineAuthorAvatar_user  ...UserName_user  __typename  id}fragment collectionUrl_collection on Collection {  id  domain  slug  __typename}fragment CollectionAvatar_collection on Collection {  name  avatar {    id    __typename  }  ...collectionUrl_collection  __typename  id}fragment EntityPresentationRankedModulePublishingTracker_entity on RankedModulePublishingEntity {  __typename  ... on Collection {    id    __typename  }  ... on User {    id    __typename  }}fragment CollectionTooltip_collection on Collection {  id  name  slug  description  subscriberCount  customStyleSheet {    header {      backgroundImage {        id        __typename      }      __typename    }    __typename    id  }  ...CollectionAvatar_collection  ...PublicationFollowButton_collection  ...EntityPresentationRankedModulePublishingTracker_entity  __typename}fragment CollectionLinkWithPopover_collection on Collection {  name  ...collectionUrl_collection  ...CollectionTooltip_collection  __typename  id}fragment PostPreviewByLineCollection_collection on Collection {  ...CollectionAvatar_collection  ...CollectionTooltip_collection  ...CollectionLinkWithPopover_collection  __typename  id}fragment PostPreviewByLine_post on Post {  creator {    ...PostPreviewByLineAuthor_user    __typename    id  }  collection {    ...PostPreviewByLineCollection_collection    __typename    id  }  __typename  id}fragment PostPreviewInformation_post on Post {  readingTime  isLocked  ...Star_post  ...usePostPublishedAt_post  __typename  id}fragment StreamPostPreviewContent_post on Post {  id  title  previewImage {    id    __typename  }  extendedPreviewContent {    subtitle    __typename  }  ...StreamPostPreviewImage_post  ...PostPreviewFooter_post  ...PostPreviewByLine_post  ...PostPreviewInformation_post  __typename}fragment PostScrollTracker_post on Post {  id  collection {    id    __typename  }  sequence {    sequenceId    __typename  }  __typename}fragment usePostUrl_post on Post {  id  creator {    ...userUrl_user    __typename    id  }  collection {    id    domain    slug    __typename  }  isSeries  mediumUrl  sequence {    slug    __typename  }  uniqueSlug  __typename}fragment PostPreviewContainer_post on Post {  id  extendedPreviewContent {    isFullContent    __typename  }  visibility  pinnedAt  ...PostScrollTracker_post  ...usePostUrl_post  __typename}fragment StreamPostPreview_post on Post {  id  ...StreamPostPreviewContent_post  ...PostPreviewContainer_post  __typename}fragment InlineFeed_homeFeedItem on HomeFeedItem {  feedId  moduleSourceEncoding  reason  postProviderExplanation {    ...StreamPostPreview_postProviderExplanation    __typename  }  post {    ...StreamPostPreview_post    __typename    id  }  __typename}",
        "variables": {
            "forceRank": False,
            "paging": {
                "limit": 5,
            }}

    }]

cookies = {
    "uid": uid,
    "sid": sid,
    "xsrf": xsrf_token
}

def getting_info():
    output = []
    for i in range(1, 151):
        if i != 1:
            payload[0]["variables"]["paging"]["to"] = str(i * 5)
        response = scraper.post(URL, json=payload, cookies=cookies, headers=headers)
        if response.status_code == 200:
            print(f"Parsing page №{i}...")
            full_data = response.json()
            items = full_data[0].get("data", {}).get("webRecommendedFeed", {}).get("items", [])
            for item in items:
                output.append({
                    "title": item.get("post").get("title"),
                    "subtitle": item.get("post").get("extendedPreviewContent").get("subtitle"),
                    "rating": item.get("post").get("clapCount"),
                    "postId": item.get("post").get("id"),
                    "link": item.get("post").get("mediumUrl"),
                })
        else:
            print("Something went wrong.", response.status_code)
    return output

def saving_info(info):
    with open("data.json", "a", encoding="utf-8") as f:
        json.dump(info, f, ensure_ascii=False, indent=4)

def parser():
    info = getting_info()
    saving_info(info)
    print("End")
parser()