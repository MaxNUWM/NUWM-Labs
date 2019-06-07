using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.PostProcessing;

public class SwithPostProcess : MonoBehaviour
{
    public PostProcessingProfile normal, underwater;
    private PostProcessingBehaviour camImageFx;
    // Start is called before the first frame update
    void Start()
    {
        camImageFx = FindObjectOfType<PostProcessingBehaviour>();
    }

    void OnTriggerEnter(Collider col)
    {
        if (col.CompareTag("Player"))
        {
            camImageFx.profile = underwater;
        }
    }
    void OnTriggerExit(Collider col)
    {
        if (col.CompareTag("Player"))
        {
            camImageFx.profile = normal;
        }
    }
}
