using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class WeaponManager : MonoBehaviour
{
    [SerializeField]
    public WeaponHandler[] weapons;
    private int curWeapon;
    // Start is called before the first frame update
    void Start()
    {
        curWeapon = 0;
        weapons[curWeapon].gameObject.SetActive(true);
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Alpha1))
        {
            ToggleWeapon(0);
        }
        if (Input.GetKeyDown(KeyCode.Alpha2))
        {
            ToggleWeapon(1);
        }
        
    }

    public WeaponHandler GetCur()
    {
        return weapons[curWeapon];
    }

    void ToggleWeapon(int new_cur)
    {
        weapons[curWeapon].gameObject.SetActive(false);
        weapons[new_cur].gameObject.SetActive(true);
        curWeapon = new_cur;
    }
}
