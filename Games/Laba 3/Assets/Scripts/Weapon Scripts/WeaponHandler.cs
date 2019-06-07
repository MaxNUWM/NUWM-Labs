using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class WeaponHandler : MonoBehaviour
{
    public Animator anim;
    public float range;
    public float damage;
    private GameObject mainCam;

    [SerializeField]
    private GameObject muzzleFlash;
    private GameObject targetPoint;

    private int count = 0;

    void Start()
    {
        mainCam =  GameObject.FindWithTag("MainCamera");
    }

    public void Fire()
    {
        anim.SetTrigger("Fire");
        RaycastHit hit;
        if (Physics.Raycast(mainCam.transform.position, mainCam.transform.forward, out hit, range))
        {
            if (hit.transform.name == "Cannibal")
            {
                hit.transform.gameObject.GetComponent<EnemyController>().takeDamage(damage);
                print("Hit for " + damage);
                print("Hit " + count + " times!");
                count += 1;
            }
            else
            {
                print("Miss! Curent hit rate" + count + " times!");
                //print("Hit target " + hit.transform.name + " times!");
            }
        }
    }

    void ApplyMuzzleFlash()
    {
        muzzleFlash.SetActive(true);
    }

    void RemoveMuzzleFlash()
    {
        muzzleFlash.SetActive(false);
    }
    void ApplyTargetPoint()
    {
        targetPoint.SetActive(true);
    }
    void RemoveTargetPoint()
    {
        if (targetPoint.activeInHierarchy)
        {
            targetPoint.SetActive(false);
        }
       
    }
}
