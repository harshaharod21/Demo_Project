# Demo_Project
Demo project

The screenshots are uploaded in the screeshots folder.

Note: 
- install markdown-to-jsx for neat and clean parsing.

- Install Node.js to get npm


## Prompting Strategies

The following prompting strategies have been employed to guide the multimodal LLM in describing features based on screenshots:

### Prompt Template

```text
First, identify features in these screenshots and provide a brief description. Understand what each specific tab and section does according to a user who can use that feature. Guide them on how they can use it. If more than one image is uploaded, proceed with this explanation one by one and then address the user-provided context.

Note: Do not output "User given context" and "Output" strictly.

Examples for your understanding:

Example 1:
- User given context: Explain to me how can I find my bookings?
- Output: The bookings tab is located to the right of the home tab in the bottom section. Please find your bookings there and for more information, select the help tab.

Example 2:
- User given context: How can I change my personal information?
- Output: Find the My Account tab in the bottom section. This can help you in changing your personal information. Provide me with the screenshot of the My Account tab so that I can assist further.

User given context: {context}
```


## Explanation

To guide the multimodal LLM in describing features from screenshots, we use the following prompting strategy:

1. **Feature Identification**: The model is asked to identify and describe features in the provided screenshots.

2. **User Guidance**: It explains how each feature can be used from a user's perspective.

3. **Handling Multiple Images**: For multiple images, the model processes each one sequentially and then addresses any additional user-provided context.

4. **Contextual Relevance**: The prompt incorporates user-provided context to tailor the explanation to specific questions or needs.



